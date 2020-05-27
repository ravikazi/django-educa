from django.urls import reverse_lazy
#from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from django.views.generic.list import CreateView, UpdateView, DeleteView
#from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from braces.views import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Course

@login_required
def dashboard(request):
	# Display all actions by default
	actions = Action.objects.all().exclude(user=request.user)
	following_ids = request.user.following.values_list('id', flat=True)
	if following_ids:
		# if user is following others, retrieve only their actions()
		action = actions.filter(user_id__in=following_ids).select_related('user', 'user__profie').prefetch_related('target')
	actions = actions[:10]  
	return render(request, 'account/dashboard.html', {'section':dashboard,'actions':actions})

class ManageCourseListView(ListView):
	model = Course
	template_name = 'courses/manage/course/list.html'

class OwnerMixin(object):
	def get_queryset(self):
		qs = super(OwnerMixin, self).get_queryset()
		return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
	model = Course


class OwnerCourseEditMixin(OwnerCourseMixin,OwnerEditMixin):
	fields = ['subject','title','slug', 'overview']
	success_url  =reverse_lazy('manage_course_list')
	template_name = 'courses/manage/course/form.html'


class ManageCourseListView(OwnerCourseMixin,ListView):
	template_name = 'courses/manage/course/list.html'


class CourseCreateView(PermissionRequiredMixin,OwnerCourseEditMixin,CreateView):
	permission_required = 'courses.add_course' 


class CourseUpdateView(PermissionRequiredMixin,OwnerCourseEditMixin,UpdateView):
	permission_required = 'courses.change_course' 


class CourseDeleteView(PermissionRequiredMixin,OwnerCourseEditMixin,DeleteView):
	success_url = reverse_lazy('manage_course_list')
	template_name = 'courses/manage/course/delete.html'
	#template_name = 'courses/manage/module/formset.html'
	permission_required = 'courses.delete_course'