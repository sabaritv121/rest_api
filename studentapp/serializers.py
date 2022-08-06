from rest_framework import serializers

from studentapp.models import Student, School, Course, Login


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ="__all__"
        # fields = (
        #     'user',
        #     'name',
        #     'address',
        #
        # )
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields ="__all__"



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields ="__all__"




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields ="__all__"

