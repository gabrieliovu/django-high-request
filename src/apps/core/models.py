from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=10)


class Teacher(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name="students"
    )


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="schedules"
    )


class Schedule(models.Model):
    student_class = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name="schedules"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="schedules"
    )
    day_of_week = models.IntegerField()
    hour = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=["day_of_week", "hour"]),
            models.Index(fields=["student_class"]),
        ]
