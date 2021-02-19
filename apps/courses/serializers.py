
from django.utils.translation import ugettext as _
from rest_framework import serializers

from rest_framework.exceptions import ValidationError


from . import models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'
    

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'

class LessonQuestionSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Lesson
        fields = '__all__'
    

    def get_questions(self,instance):
        questions = models.Question.objects.filter(lesson=instance)
        if len(questions) > 0:
            return QuestionSerializer(questions,many=True).data
        return []

class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserCourse
        fields = '__all__'

class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserLesson
        fields = '__all__'


class QuestionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionUser
        fields = '__all__'

        


 