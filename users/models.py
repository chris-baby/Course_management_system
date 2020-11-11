from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class Admin(models.Model):
    """
    管理员
    """
    admin_login = models.CharField('登录账户',max_length=12,null=False,unique=True)
    admin_password =models.CharField('账户密码',max_length=20,null=False)
    Permission = models.CharField('管理权限',max_length=20,null=False)

    class Meta:
        verbose_name = "管理员信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.admin_login



class UserProfile(AbstractUser):
    """
    学生信息
    """
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    name = models.CharField("姓名",max_length=10, null=False)
    gender = models.CharField("性别",max_length=6, choices=GENDER_CHOICES)
    birthday = models.DateField("出生日期", null=True)
    address = models.CharField('家庭住址',max_length=50,null=True)
    mobile = models.CharField("电话",max_length=11,null=False)

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Teacher(models.Model):
    """
    老师表
    """
    name = models.CharField('老师姓名',max_length=10,null=False)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name


class Course(models.Model):
    """
    课程信息
    """
    no = models.IntegerField('课程号')
    name = models.CharField('课程名',max_length=10,null=False)
    desc = models.CharField("课程描述", max_length=100)
    type = models.CharField("课程类别",max_length=10,null=False)
    time = models.IntegerField('学习时长',default=0)
    teacher = models.ForeignKey(Teacher, verbose_name='老师', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

class Grade(models.Model):
    """
    班级表
    """
    grade = models.SmallIntegerField("班级",null=False)
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """
    用户课程
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name