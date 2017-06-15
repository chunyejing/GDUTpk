"""gdutpk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from pingke import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

	url(r'^$', views.index, name='index'),
	url(r'^course/(?P<course_id>[0-9]+)/$', views.course, name='course')
#	url(r'^teacher/(?P<teacher_id>[0-9]+/$', view.teacher, name='teacher')
#	url(r'^student/(?P<student_id>[0-9]+/$', view.student, name='student')
#	url(r'^course_type/(?P<course_type_id>[0-9]+)/$', view.course_type_xuanxiu, name='course_type')
]
