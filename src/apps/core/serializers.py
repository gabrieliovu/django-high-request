from rest_framework import serializers

from .models import Class, Schedule, Subject, Teacher


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["name"]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["name"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name"]


class ScheduleSerializer(serializers.ModelSerializer):
    student_class = ClassSerializer()
    subject = SubjectSerializer()
    teacher = TeacherSerializer(source="subject.teacher")

    class Meta:
        model = Schedule
        fields = ["student_class", "subject", "day_of_week", "hour", "teacher"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["student_class"]["student_count"] = instance.student_count
        return representation
