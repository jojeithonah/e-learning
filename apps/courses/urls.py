from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('courses',views.CourseView)
router.register('lesson',views.LessonView)
router.register('question',views.QuestionView)
router.register('user-courses',views.UserCourseView)
router.register('student-courses',views.CourseStudentView)
router.register('user-lesson',views.UserLessonView)
router.register('student-lesson',views.LessonStudentView)
router.register('answer-questions',views.AnswerQuestionView)



urlpatterns = [

]

urlpatterns += router.urls
