import random

from core.models import Class, Schedule, Student, Subject, Teacher
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Populate all tables with initial data"

    def handle(self, *args, **kwargs):
        self.populate_student_classes()
        self.populate_teachers()
        self.populate_subjects()
        self.populate_students()
        self.populate_schedules()

    def populate_student_classes(self):
        if not Class.objects.exists():
            for i in range(1, 31):
                Class.objects.create(name=f"Class {i}")
            self.stdout.write(self.style.SUCCESS("Successfully populated StudentClass"))

    def populate_teachers(self):
        if not Teacher.objects.exists():
            for i in range(1, 41):
                Teacher.objects.create(name=f"Teacher {i}")
            self.stdout.write(self.style.SUCCESS("Successfully populated Teacher"))

    def populate_subjects(self):
        if not Subject.objects.exists():
            teachers = list(Teacher.objects.all())
            for i in range(1, 31):
                teacher = random.choice(teachers)
                Subject.objects.create(name=f"Subject {i}", teacher=teacher)
            self.stdout.write(self.style.SUCCESS("Successfully populated Subject"))

    def populate_students(self):
        if not Student.objects.exists():
            student_classes = list(Class.objects.all())
            for student_class in student_classes:
                for i in range(1, 21):  # Assuming each class has 20 students
                    Student.objects.create(
                        name=f"Student {i} of {student_class.name}",
                        student_class=student_class,
                    )
            self.stdout.write(self.style.SUCCESS("Successfully populated Students"))

    def populate_schedules(self):
        if not Schedule.objects.exists():
            student_classes = list(Class.objects.all())
            subjects = list(Subject.objects.all())
            for student_class in student_classes:
                for day in range(5):  # Monday to Friday
                    for hour in range(8, 16):  # 8 AM to 3 PM
                        subject = random.choice(subjects)
                        Schedule.objects.create(
                            student_class=student_class,
                            subject=subject,
                            day_of_week=day,
                            hour=hour,
                        )
            self.stdout.write(self.style.SUCCESS("Successfully populated Schedule"))
