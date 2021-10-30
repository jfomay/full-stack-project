"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf`
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views as myapp_views
from movies import views as movies_views
from courses.views import CoursesView, CreateCourseView, StudentApiView


urlpatterns = [
    path('', myapp_views.index, name='index'),
    path('my_name/', myapp_views.my_name, name='my_name'),
    path('movies/list/', movies_views.list, name='movies_list'),
    path('movies/detail/<int:movie_id>/', movies_views.detail, name='movie_detail'),
    path('movies/create/', movies_views.create, name='movie_create'),
    path('movies/update/<int:movie_id>/', movies_views.update, name='movie_update'),
    path('courses/list/', CoursesView.as_view(), name="course_list"),
    path('courses/create/', CreateCourseView.as_view(), name ='create_course' ),
    path('courses/<int:course_id>/students', StudentApiView.as_view(), name='students_list'),
    path('admin/', admin.site.urls),
]
 