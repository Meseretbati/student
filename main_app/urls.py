"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views, hod_views, staff_views, student_views
urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("get_user_details/", views.getUserDetails, name='get_user_details'),
    path("logout_user/", views.logout_user, name='user_logout'),
    path("admin_home/", hod_views.admin_home, name='admin_home'),
    path("add_staff/", hod_views.add_staff, name='add_staff'),
    path("add_course/", hod_views.add_course, name='add_course'),
    path("add_session/", hod_views.add_session, name='add_session'),
    path("manage_session/", hod_views.manage_session, name='manage_session'),
    path("edit_session/<int:session_id>",
         hod_views.edit_session, name='edit_session'),
    path("add_student/", hod_views.add_student, name='add_student'),
    path("add_subject/", hod_views.add_subject, name='add_subject'),
    path("manage_staff/", hod_views.manage_staff, name='manage_staff'),
    path("manage_student/", hod_views.manage_student, name='manage_student'),
    path("manage_course/", hod_views.manage_course, name='manage_course'),
    path("manage_subject/", hod_views.manage_subject, name='manage_subject'),
    path("edit_staff/<int:staff_id>", hod_views.edit_staff, name='edit_staff'),
    path("edit_student/<int:student_id>",
         hod_views.edit_student, name='edit_student'),
    path("edit_course/<int:course_id>",
         hod_views.edit_course, name='edit_course'),
    path("edit_subject/<int:subject_id>",
         hod_views.edit_subject, name='edit_subject'),
    # Staff
    path("staff_home/", staff_views.staff_home, name='staff_home'),
    path("staff_take_attendance/", staff_views.staff_take_attendance,
         name='staff_take_attendance'),
    path("staff_update_attendance/", staff_views.staff_update_attendance,
         name='staff_update_attendance'),
    path("get_students", staff_views.get_students, name='get_students'),
    path("get_attendance", staff_views.get_attendance, name='get_attendance'),
    path("get_student_attendance", staff_views.get_student_attendance,
         name='get_student_attendance'),
    path("save_attendance", staff_views.save_attendance, name='save_attendance'),
    path("update_attendance", staff_views.update_attendance,
         name='update_attendance'),

    # Student
    path("student_home/", student_views.student_home, name='student_home'),

]
