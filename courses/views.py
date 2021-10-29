from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from courses.models import Course, Student
from django.http import JsonResponse


# Create your views here.
class CoursesView(ListView):
    model = Course
    template_name = 'courses/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

class CreateCourseView(CreateView):
    model = Course
    fields = ['name', 'semester']
    success_url = '/courses/list'

class StudentApiView(View):
	def get(self, *args, **kwargs):
		course_id = kwargs.get('course_id')
		course = Course.objects.get(id=course_id)
		context = {'course': course, 'students': course.student_set.all()}
		return render(self.request, 'courses/student_list.html', context)

	def post(self, *args, **kwargs):
		data = self.request.POST
		first_name = data.get('first_name')
		last_name = data.get ('last_name')
		course_id = kwargs.get('course_id')
		course = Course.objects.get(id=course_id)

		student = Student.objects.create(first_name=first_name, last_name=last_name, course=course)

		response_data = {}
		response_data['first_name'] = student.first_name
		response_data['last_name'] = student.last_name

		return JsonResponse(response_data)


