from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from .factories import ScheduleFactory, StudentFactory


class ScheduleListViewTests(TestCase):
    def setUp(self):
        self.schedule1 = ScheduleFactory(day_of_week=1, hour=9)
        self.schedule2 = ScheduleFactory(day_of_week=1, hour=10)
        self.schedule3 = ScheduleFactory(
            day_of_week=2, hour=11, student_class__name="5A"
        )
        StudentFactory.create_batch(2, student_class=self.schedule1.student_class)
        StudentFactory.create_batch(3, student_class=self.schedule2.student_class)
        StudentFactory.create_batch(4, student_class=self.schedule3.student_class)

    def test_schedule_list_view(self):
        url = reverse("schedule-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["student_class"]["student_count"], 2)
        self.assertEqual(response.data[1]["student_class"]["student_count"], 3)
        self.assertEqual(response.data[2]["student_class"]["student_count"], 4)

    def test_schedule_list_view_ordering(self):
        url = reverse("schedule-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["day_of_week"], 1)
        self.assertEqual(response.data[1]["day_of_week"], 1)
        self.assertEqual(response.data[2]["day_of_week"], 2)

    def test_schedule_list_view_filtering(self):
        url = reverse("schedule-list") + "?day_of_week=1"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["day_of_week"], 1)
        self.assertEqual(response.data[1]["day_of_week"], 1)

    def test_schedule_list_view_invalid_filter(self):
        url = reverse("schedule-list") + "?day_of_week=invalid"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_schedule_list_view_empty_result(self):
        url = reverse("schedule-list") + "?day_of_week=3"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_schedule_list_view_fields(self):
        url = reverse("schedule-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("student_class", response.data[0])
        self.assertIn("subject", response.data[0])
        self.assertIn("day_of_week", response.data[0])
        self.assertIn("hour", response.data[0])

    def test_schedule_list_view_for_today(self):
        url = reverse("schedule-list") + "?for_today=true"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["day_of_week"], timezone.now().weekday())
        self.assertEqual(response.data[1]["day_of_week"], timezone.now().weekday())

    def test_schedule_list_view_class_name_filter(self):
        url = reverse("schedule-list") + "?class_name=5A"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["student_class"]["name"], "5A")

    def test_schedule_list_view_combined_filters(self):
        url = reverse("schedule-list") + "?for_today=true&class_name=5A"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["day_of_week"], timezone.now().weekday())
        self.assertEqual(response.data[0]["student_class"]["name"], "5A")
