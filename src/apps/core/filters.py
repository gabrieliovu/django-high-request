from datetime import datetime

from django.core.cache import cache
from django_filters import rest_framework as filters

from .models import Schedule


class ScheduleFilter(filters.FilterSet):
    class_name = filters.CharFilter(
        field_name="student_class__name", lookup_expr="exact"
    )
    for_today = filters.BooleanFilter(method="filter_for_today")

    class Meta:
        model = Schedule
        fields = ["class_name", "day_of_week", "hour"]

    def filter_for_today(self, queryset, name, value):
        if value:
            today = datetime.today().weekday()
            class_name = self.data.get("class_name", "")
            cache_key = f"schedules_for_today_{today}_{class_name}"

            cached_queryset = cache.get(cache_key)

            if cached_queryset is None:
                filtered_queryset = queryset.filter(day_of_week=today)
                if class_name:
                    filtered_queryset = filtered_queryset.filter(
                        student_class__name=class_name
                    )
                cache.set(
                    cache_key, filtered_queryset, timeout=60 * 60
                )  # Cache for 1 hour
                cached_queryset = filtered_queryset

            return cached_queryset
        return queryset
