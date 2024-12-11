import logging

from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import ScheduleFilter
from .models import Schedule
from .serializers import ScheduleSerializer

logger = logging.getLogger("core")


class ScheduleListView(generics.ListAPIView):
    queryset = (
        Schedule.objects.select_related("student_class", "subject", "subject__teacher")
        .prefetch_related("student_class__students")
        .annotate(student_count=Count("student_class__students"))
        .only(
            "student_class__name",
            "subject__name",
            "subject__teacher__name",
            "day_of_week",
            "hour",
        )
        .order_by("day_of_week", "hour")
    )
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter
