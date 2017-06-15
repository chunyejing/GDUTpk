from django.shortcuts import render, get_object_or_404

from .models import *

# Create your views here.

def index(request):
	latest_reviews_list = Review.objects.query_by_time()
	context = {'reviews': latest_reviews_list}
	return render(request, 'index.html', context)

def course(request, course_id):
	course = get_object_or_404(Course, id=course_id)
	reviews = course.review_set.all()
	return render(request, 'course.html', 
			{'reviews': reviews,
			 'course': course,
			}
			)

#def course_type(request, course_type_id):
#	courses = Course.objects.filter(course_type.id = course_type_id).order_by('name')
#	return render(request, 'course_type.html, 'courses': courses)
