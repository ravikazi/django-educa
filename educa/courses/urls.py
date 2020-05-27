from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from account import views as ac_views

urlpatterns = [
    path("mine/", views.ManageCourseListView.as_view(), name="manage_course_list"),
    # path("create/", views.CourseCreateView.as_view(), name="course_create"),
    # path("<id>/edit", views.CourseUpdateView.as_view(), name="course_edit"),
    # path("<id>/delete", views.CourseDeleteView.as_view(), name="course_delete"),
    # path("<id>/module", views.CourseModuleUpdateView.as_view(), name="course_module"),

    # path("module/<module_id>/content/<model_name>/create", views.ContentCreateUpdateView.as_view(), name="module_content_create"),
    # path("module/<module_id>/content/<model_name>/<id>", views.ContentCreateUpdateView.as_view(), name="module_content_update"),
    # path("content/<id>/delete", views.ContentDeleteView.as_view(), name="module_content_delete"),
    # path("module/<module_id>", views.ModuleContentListView.as_view(), name="module_content_list"),
    # path("module/order", views.ModuleOrderView.as_view(), name="module_order"),
    # path("content/order", views.ContentOrderView.as_view(), name="content_order"),
]