from django.utils.translation import ugettext as _

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import filters as df
from rest_framework.response import Response


from django_filters import rest_framework as filters

from . import models
from . import serializers
from . import permissions
from . import mixins
from . import utils

class CourseView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,permissions.IsTeacher]
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LessonView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,permissions.IsTeacher]
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    filter_backends = (df.OrderingFilter, df.SearchFilter, filters.DjangoFilterBackend)
    filterset_fields = ('course',)


class QuestionView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,permissions.IsTeacher]
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    filter_backends = (df.OrderingFilter, df.SearchFilter, filters.DjangoFilterBackend)
    filterset_fields = ('lesson',)

class UserCourseView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,permissions.IsTeacher]
    queryset = models.UserCourse.objects.all()
    serializer_class = serializers.UserCourseSerializer

class UserLessonView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,permissions.IsTeacher]
    queryset = models.UserLesson.objects.all()
    serializer_class = serializers.UserLessonSerializer

class CourseStudentView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Course.get_student_courses(user)

class LessonStudentView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.LessonQuestionSerializer
        return serializers.LessonSerializer

    def get_queryset(self):
        user = self.request.user
        course = self.request.GET.get('course')
        if course:
            return models.Lesson.get_student_lesson(user,course)
        else:
            return  models.Lesson.objects.all()

class AnswerQuestionView(mixins.CreateListMixin, viewsets.ModelViewSet):
    queryset = models.QuestionUser.objects.all()
    serializer_class = serializers.QuestionUserSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return serializers.QuestionUserSerializer
    #     return self.serializer_class
    
    def perform_create(self, serializer):
        item = serializer.save()
        utils.validate_answer(item)
        return item
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = serializers.QuestionUserSerializer(instance,many=True)
        return Response(instance_serializer.data)


    


        

