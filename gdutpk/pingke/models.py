from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#yonghu

#youke
class GdutGuest(models.Model):
#	id=
	username = models.CharField(max_length=200)
	email = models.EmailField()
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now=True)
	review_count = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.username

class GdutUser(AbstractUser):
	gender = models.CharField(max_length=20, choices=(('male','male'),('female','female'),('unknown','unknown')),default='unknown')
	identity = models.CharField(max_length=10, choices=(('teacher','teacher'),('student','student')), default='student')
	
#	gender = models.CharField(max_length=20, choices=['male','female','unknown'], default='unknown')
#	identity = models.CharField(max_length=20, choices=['teacher','student'], default='student')
	homepage = models.CharField(max_length=200, blank=True)
	description = models.TextField()
	avatar = models.ImageField(upload_to='image', default='/static/image/user.png')

class Dept(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	name_eng = models.CharField(max_length=200, blank=True)
	code = models.CharField(max_length=20, blank=True)
	
	def __unicode__(self):
		return self.name
class Major(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	name_eng = models.CharField(max_length=200, blank=True)
	code = models.CharField(max_length=20, blank=True)
	def __unicode__(self):
		return self.name

'''
class DeptClass(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	dept = models.ForeignKey(Dept)	

class Student(models.Model):
	sno = models.CharField(primary_key=True)
	name = models.CharField(80)
	email = models.CharField()
'''	
	
class Teacher(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=80)
	email = models.CharField(max_length=80, blank=True)
	def __unicode__(self):
		return self.name

class Course_type(models.Model):
	name = models.CharField(max_length=80)

class Course(models.Model):
#	id = models.IntegerField(primary_key=True, primary_key=True)
	name = models.CharField(max_length=80)
	course_type = models.ForeignKey(Course_type, blank=True)

	dept = models.ManyToManyField(Dept, blank=True)
	majoy = models.ManyToManyField(Major, blank=True)

	teacher = models.ManyToManyField(Teacher, default="unknow")
	profile = models.TextField(blank=True)

	is_good = models.BooleanField(default=False)
	is_show = models.BooleanField(default=False)
	def __unicode__(self):
		return self.name

class ReviewManager(models.Manager):
	def query_by_time(self):
		query = self.get_queryset().order_by('publish_time')
		return query

class Review(models.Model):
	content = models.TextField()

	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	guest = models.ForeignKey(GdutGuest, blank=True)
	author = models.ForeignKey(GdutUser, blank=True)
	course = models.ForeignKey(Course)

	is_good = models.BooleanField(default=False)
	is_show = models.BooleanField(default=False)

	objects = ReviewManager()

	def __unicode__(self):
		return self.course.name
