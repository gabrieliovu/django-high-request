import factory

from ..models import Class, Schedule, Student, Subject, Teacher


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    name = "John Doe"


class SubjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subject

    name = "Math"
    teacher = factory.SubFactory(TeacherFactory)


class StudentClassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Class

    name = "Class 1"


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    name = factory.Sequence(lambda n: f"Student {n}")
    student_class = factory.SubFactory(StudentClassFactory)


class ScheduleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Schedule

    student_class = factory.SubFactory(StudentClassFactory)
    subject = factory.SubFactory(SubjectFactory)
    day_of_week = 1
    hour = 9
