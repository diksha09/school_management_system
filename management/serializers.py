from django.contrib.auth.models import User
from rest_framework import serializers
from .models import SchoolUser, Klass, Subject, Div, Student, StudentFee, Teacher, Department, StudAtt, TeachAtt, AssiTeacher


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

        
class SchoolUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SchoolUser
        fields = ('__all__')

        
class KlassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Klass
        fields = ('__all__')


class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ('__all__')

        
class DivSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Div
        fields = ('__all__')

        
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('__all__')


class StudAttSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudAtt
        fields = ('__all__')

        
class StudentFeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentFee
        fields = ('__all__')

        
class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ('__all__')

        
class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ('__all__')
        
        
class TeachAttSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TeachAtt
        fields = ('__all__')

        
class AssiTeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AssiTeacher
        fields = ('__all__')
