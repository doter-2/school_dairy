from .models import Users, Schedule, Grades, Subject, Attendance, Payment
from rest_framework import serializers

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'student_class', 'is_active', 'is_staff', 'avatar']

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'student_class', 'is_active', 'is_staff', 'avatar']

    def get_avatar(self, obj):
        if not obj.avatar:
            return None
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.avatar.url)
        return obj.avatar.url
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id',
            'subject',
            'date',
            'start_time',
            'end_time',
            'classroom',
            'teacher',
            'class_name'
        ]
    
def get_student_name(self, obj):
    return getattr(obj.student, "username", None)

def get_subject_name(self, obj):
    return getattr(obj.subject, "name", None)
class GradesSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()

    class Meta:
        model = Grades
        fields = [
            'id',
            'student',
            'student_name',
            'subject',
            'subject_name',
            'grade',
            'date',
            'lesson_topic',
        ]

def get_student_name(self, obj):
    return getattr(obj.student, "username", None)

def get_subject_name(self, obj):
    return getattr(obj.subject, "name", None)
class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = [
            'id',
            'student',
            'student_name',
            'subject',
            'subject_name',
            'attendance',
            'date',
        ]

def get_student_name(self, obj):
    return getattr(obj.student, "username", None)
class PaymentSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = [
            'id',
            'student',
            'student_name',
            'date_pay',
            'month',
            'paid',
        ]

    def get_student_name(self, obj):
        return obj.student.username if obj.student else None