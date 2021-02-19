from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext as _
from common import enums
from apps.users import models as model_user
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    previous_course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    
    @staticmethod
    def get_student_courses(user):
        acces_course = UserCourse.objects.filter(user=user).values_list('course',flat=True)
        return Course.objects.filter(pk__in=acces_course)

    

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    previous_lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True, blank=True)
    score_to_approve = models.IntegerField(_("Score to Approve"))

    def __str__(self):
        return f'{self.name}'
    
    @staticmethod
    def get_student_lesson(user,course):
        acces_lesson = UserLesson.objects.filter(user=user).values_list('lesson',flat=True)
        print(acces_lesson)
        return Lesson.objects.filter(pk__in=acces_lesson,course__id=int(course))
    
class Question(models.Model):
    TYPE_QUESTION = (
        (enums.TypeCuestion.BOOLEAN.value, _('Boolean')),
        (enums.TypeCuestion.ONE_CORRECT.value, _('Only one answer is correct')),
        (enums.TypeCuestion.MORE_ONE_CORRECT.value, _('More than one answer is correct')),
        (enums.TypeCuestion.ALL_MUST_CORRECT.value, _('More than one answer is correct and all of them must be answered correctly')),
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    question_type = models.PositiveSmallIntegerField(choices=TYPE_QUESTION,
        verbose_name=_('Type Question'),
        default=enums.TypeCuestion.BOOLEAN.value
    )
    posible_answers =  ArrayField(
            models.CharField(max_length=50, blank=False),
            size=5,
            null=True,
            blank=True
        )
    bool_answer = models.BooleanField(null=True,blank=True)
    one_answer = models.CharField(max_length=200,blank=True,null=True)
    multiple_answers = ArrayField(
            models.CharField(max_length=50),
            size=5,
            null=True,
            blank=True
        )
    score = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class QuestionUser(models.Model):
    user = models.ForeignKey(model_user.User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    bool_answer = models.BooleanField(null=True,blank=True)
    one_answer = models.CharField(max_length=200,null=True)
    multiple_answers = ArrayField(
            models.CharField(max_length=50),
            size=5,
            null=True,
            blank=True
        )
    score = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question.name}'

class UserCourse(models.Model):
    user = models.ForeignKey(model_user.User, verbose_name=_("User Course"), on_delete=models.CASCADE)
    course = models.ForeignKey("Course", verbose_name=_("Course"), on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.course.name}'

    class Meta:
        unique_together = [['user', 'course']]

class UserLesson(models.Model):
    user = models.ForeignKey(model_user.User, verbose_name=_("User Lesson"), on_delete=models.CASCADE)
    lesson = models.ForeignKey("Lesson", verbose_name=_("Lesson"), on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.lesson.name}'
    

    class Meta:
        unique_together = [['user', 'lesson']]
