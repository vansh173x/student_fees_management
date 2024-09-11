"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_reg/',admin_reg),
    path('view_operator_admin/',view_operator_admin),
    path('operator_reg/',operator_reg),
    path('student_reg_admin/',student_reg_admin),
    path('student_reg_operator/',student_reg_operator),
    path('show_admin/',show_admin),
    path('show_operator/',show_operator),
    path('show_student_admin/',show_student_admin),
    path('show_student_operator/',show_student_operator),
    path('edit_admin/',edit_admin),
    path('edit_admin_1/',edit_admin_1),
    path('edit_operator/',edit_operator),
    path('edit_operator_1/',edit_operator_1),
    path('edit_student_admin/', edit_student_admin),
    path('edit_student_admin1/', edit_student_admin1),
    path('edit_student_operator/',edit_student_operator),
    path('edit_student_operator1/', edit_student_operator1),
    path('delete_admin/',delete_admin),
    path('delete_admin_1/',delete_admin_1),
    path('delete_operator/',delete_operator),
    path('delete_operator_1/',delete_operator_1),
    path('delete_student_admin/',delete_student_admin),
    path('delete_student_admin1/',delete_student_admin1),
    path('delete_student_operator/',delete_student_operator),
    path('delete_student_operator1/',delete_student_operator1),
    path('signin/',signin),
    path('admin_home/',admin_home),
    path('operator_home/',operator_home),
    path('student_home/',student_home),
    path('auth_error/',auth_error),
    path('logout/',logout),
    path('changepass_admin/',changepass_admin),
    path('changepass_operator/',changepass_operator),
    path('changepass_student/',changepass_student),
    path('upload_photo_admin/',upload_photo_admin),
    path('upload_photo_student_admin/',upload_photo_student_admin),
    path('upload_photo_student_operator/',upload_photo_student_operator),
    path('upload_photo_operator/',upload_photo_operator),
    path('admin_profile/',admin_profile),
    path('operator_profile/',operator_profile),
    path('student_profile/',student_profile),
    path('change_photo_admin/',change_photo_admin),
    path('change_photo_operator/',change_photo_operator),
    path('change_photo_student_admin/',change_photo_student_admin),
    path('change_photo_student_operator/',change_photo_student_operator),
    path('view_student_admin/',view_student_admin),
    path('view_student_operator/',view_student_operator),
    path('course_reg/',course_reg),
    path('show_courses/',show_courses),
    path('edit_courses/',edit_courses),
    path('edit_courses_1/',edit_courses_1),
    path('delete_courses/',delete_courses),
    path('delete_courses_1/',delete_courses_1),
    path('add_courses/',add_courses),
    path('add_courses_1/',add_courses_1),
    path('pay_installment/',pay_installment),
    path('pay_installment_1/',pay_installment_1),
]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)