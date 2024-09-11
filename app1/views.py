from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.core.files.storage import FileSystemStorage
import os
import time
from datetime import date

# Create your views here.

def signin(request):
    if(request.method=="POST"):
        Email = request.POST['T1']
        Password = request.POST['T2']
        try:
            obj=login.objects.get(Email=Email,Password=Password)
            usertype = obj.usertype
            request.session['usertype'] = usertype
            request.session['Email'] = Email

            if(usertype == 'admin'):
                return HttpResponseRedirect('/admin_home/')
            elif(usertype == 'operator'):
                return HttpResponseRedirect("/operator_home/")
            elif(usertype == 'student'):
                return HttpResponseRedirect("/student_home/")
        except:
                return render(request,'signin.html',{'data':"Invalid Login Credentials"})
    else:
        return render(request,'signin.html')

def changepass_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email =  request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                old_password = request.POST['T1']
                new_password = request.POST['T2']
                confirm_new_password = request.POST['T3']

                obj = login.objects.get(Email=email)
                if (new_password == confirm_new_password and old_password == obj.Password):
                    obj.Password = new_password
                    obj.save()
                    return render(request, 'changepass_admin.html', {'name': "Success"})
                else:
                    return render(request, 'changepass_admin.html', {'name': "Invalid Password"})

            else:
                return render(request,'changepass_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def changepass_operator(request):
    if(request.session.has_key('usertype')):
        usertype=request.session['usertype']
        email=request.session['Email']
        if(usertype == 'operator'):
            if(request.method=="POST"):
                old_password = request.POST['T1']
                new_password = request.POST['T2']
                confirm_new_password = request.POST['T3']

                obj=login.objects.get(Email=email)
                if(new_password == confirm_new_password and old_password == obj.Password):
                    obj.Password=new_password
                    obj.save()
                    return render(request,'changepass_operator.html',{'name':"Success"})
                else:
                    return render(request,'changepass_operator.html',{'name':"Invalid Password"})
            else:
                return render(request,'changepass_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def changepass_student(request):
    if(request.session.has_key('usertype')):
        usertype=request.session['usertype']
        email=request.session['Email']
        if(usertype == 'student'):
            if(request.method=="POST"):

                old_password = request.POST['T1']
                new_password = request.POST['T2']
                confirm_new_password = request.POST['T3']

                obj=login.objects.get(Email=email)
                if(new_password == confirm_new_password and old_password == obj.Password):
                    obj.Password = new_password
                    obj.save()
                    return render(request,'changepass_student.html',{'name':'Success'})
                else:
                    return render(request,'changepass_student.html',{'name':"Invalid Credentials"})
            else:
                return render(request,'changepass_student.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def admin_home(request):
    if(request.session.has_key('usertype')):
        usertype =request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            return render(request,'admin_home.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def  operator_home(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            return render(request,'operator_home.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def  student_home(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'student'):
            return render(request,'student_home.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def auth_error(request):
    return render(request,'auth_error.html')

def logout(request):
    try:
        del request.session['Email']
        del request.session['usertype']
    except:
        pass
    return HttpResponseRedirect('/signin/')

def admin_reg(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                obj=admindata()
                obj1=login()

                a=request.POST['T1']
                b=request.POST['T2']
                c=request.POST['T3']
                d=request.POST['T4']
                e=request.POST['T5']
                f='admin'

                obj.Name=a
                obj.Address=b
                obj.Contact=c
                obj.Email=d

                obj1.Email=d
                obj1.Password=e
                obj1.usertype=f

                obj.save()
                obj1.save()

                return render(request,'admin_reg.html',{'data':"DATA IS SAVED"})
            else:
                return render(request,'admin_reg.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def operator_reg(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                obj=operator()
                obj1=login()

                a=request.POST['T1']
                b=request.POST['T2']
                c=request.POST['T3']
                d=request.POST['T4']
                e=request.POST['T5']
                f='operator'

                obj.Name=a
                obj.Address=b
                obj.Contact=c
                obj.Email=d

                obj1.Email=d
                obj1.Password=e
                obj1.usertype=f

                obj.save()
                obj1.save()

                return render(request,'operator_reg.html',{'data':"DATA IS SAVED"})
            else:
                return render(request,'operator_reg.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def student_reg_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):

                obj=student()
                obj1=login()

                a=request.POST['T1']
                b=request.POST['T2']
                c=request.POST['T3']
                d=request.POST['T4']
                e=request.POST['T5']
                f=request.POST['T6']
                g='student'

                obj.Name=a
                obj.Gender=b
                obj.Address=c
                obj.Contact=d
                obj.Email=e

                obj1.Email=e
                obj1.Password=f
                obj1.usertype=g

                obj.save()
                obj1.save()

                return render(request,'student_reg_admin.html',{'data':"DATA IS SAVED"})
            else:
                return render(request,'student_reg_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def student_reg_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method=="POST"):

                obj=student()
                obj1=login()

                a=request.POST['T1']
                b=request.POST['T2']
                c=request.POST['T3']
                d=request.POST['T4']
                e=request.POST['T5']
                f=request.POST['T6']
                g='student'

                obj.Name=a
                obj.Gender=b
                obj.Address=c
                obj.Contact=d
                obj.Email=e

                obj1.Email=e
                obj1.Password=f
                obj1.usertype=g

                obj.save()
                obj1.save()

                return render(request,'student_reg_operator.html',{'data':"DATA IS SAVED"})
            else:
                return render(request,'student_reg_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def show_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            obj=admindata.objects.all()
            obj1=photodata.objects.filter(Email=email)
            return render(request,'show_admin.html',{'data':obj,'data1':obj1})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def show_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            obj=operator.objects.all()
            return render(request,'show_operator.html',{'data':obj})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def show_student_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            obj=student.objects.all()
            return render(request,'show_student_admin.html',{'data':obj})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def show_student_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            obj=student.objects.all()
            return render(request,'show_student_operator.html',{'data':obj})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_admin(request):
    if(request.session.has_key('usertype')):
        usertype  = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                Email=request.POST['H1']
                obj=admindata.objects.filter(Email=Email)
                return render(request,'edit_admin.html',{'data':obj})
            else:
                return render(request,'edit_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_admin_1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                Name = request.POST['T1']
                Address = request.POST['T2']
                Contact = request.POST['T3']
                Email = request.POST['T4']

                obj=admindata.objects.get(Email=Email)

                obj.Name=Name
                obj.Address=Address
                obj.Contact=Contact

                obj.save()
                return render(request,'edit_admin_1.html',{'name':'SAVED'})
            else:
                return render(request,'edit_admin_1.html',{'name':'Data changes are not saved'})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                Email=request.POST['H1']
                obj=operator.objects.filter(Email=Email)
                return render(request,'edit_operator.html',{'data':obj})
            else:
                return render(request,'edit_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_operator_1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                Name = request.POST['T1']
                Address = request.POST['T2']
                Contact = request.POST['T3']
                Email = request.POST['T4']

                obj=operator.objects.get(Email=Email)

                obj.Name=Name
                obj.Address=Address
                obj.Contact=Contact

                obj.save()
                return render(request,'edit_operator_1.html',{'name':'SAVED'})
            else:
                return render(request,'edit_operator_1.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_student_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                Email=request.POST['H1']
                obj=student.objects.filter(Email=Email)
                return render(request,'edit_student_admin.html',{'data':obj})
            else:
                return render(request,'edit_student_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_student_admin1(request):
    if(request.session.has_key('usertype')):
        usretype = request.session['usertype']
        email = request.session['Email']
        if(usretype == 'admin'):
            if(request.method=="POST"):
                Name = request.POST['T1']
                Gender = request.POST['T2']
                Address = request.POST['T3']
                Contact = request.POST['T4']
                Email = request.POST['T5']

                obj=student.objects.get(Email=Email)

                obj.Name=Name
                obj.Gender=Gender
                obj.Address=Address
                obj.Contact=Contact

                obj.save()
                return render(request,'edit_student_admin1.html',{'name':'SAVED'})
            else:
                return render(request,'edit_student_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def edit_student_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method=="POST"):
                Email=request.POST['H1']
                obj=student.objects.filter(Email=Email)
                return render(request,'edit_student_operator.html',{'data':obj})
            else:
                return render(request,'edit_student_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_student_operator1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method=="POST"):
                Name = request.POST['T1']
                Gender = request.POST['T2']
                Address = request.POST['T3']
                Contact = request.POST['T4']
                Email = request.POST['T5']

                obj=student.objects.get(Email=Email)

                obj.Name=Name
                obj.Gender=Gender
                obj.Address=Address
                obj.Contact=Contact

                obj.save()
                return render(request,'edit_student_operator1.html',{'name':'SAVED'})
            else:
                return render(request,'edit_student_operator1.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_admin(request):
    if(request.method=="POST"):
        Email = request.POST['H1']
        obj=admindata.objects.filter(Email=Email)
        return render(request,'delete_admin.html',{'data':obj})

def delete_admin_1(request):
    if(request.method=="POST"):
        Email = request.POST["Email"]
        obj=admindata.objects.get(email=Email)
        obj1=login.objects.get(email=Email)
        obj.delete()
        obj1.delete()

        return render(request,'delete_admin_1.html',{'name':'DELETED'})

def delete_operator(request):
    if(request.method=="POST"):
        Email = request.POST['H1']
        obj=operator.objects.filter(Email=Email)

        return render(request,'delete_operator.html',{'data':obj})

def delete_operator_1(request):
    if(request.method=="POST"):
        Email = request.POST["Email"]
        obj=operator.objects.get(Email=Email)
        obj1=login.objects.get(Email=Email)
        obj.delete()
        obj1.delete()

        return render(request,'delete_operator_1.html',{'name':'DELETED'})

def delete_student_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                Email = request.POST['H1']
                obj=student.objects.filter(Email=Email)

                return render(request,'delete_student_admin.html',{'data':obj})
            else:
                return render(request,'delete_student_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_student_admin1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                Email = request.POST["Email"]
                obj=student.objects.get(Email=Email)
                obj1=login.objects.get(Email=Email)
                obj.delete()
                obj1.delete()

                return render(request,'delete_student_admin1.html',{'name':'DELETED'})
            else:
                return render(request,'delete_student_admin1')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_student_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method=="POST"):
                Email = request.POST['H1']
                obj=student.objects.filter(Email=Email)

                return render(request,'delete_student_operator.html',{'data':obj})
            else:
                return render(request,'delete_student_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_student_operator1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method=="POST"):
                Email = request.POST["Email"]
                obj=student.objects.get(Email=Email)
                obj1=login.objects.get(Email=Email)
                obj.delete()
                obj1.delete()

                return render(request,'delete_student_operator1.html',{'name':'DELETED'})
            else:
                return render(request,'delete_student_operator1')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def admin_profile(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == 'POST'):
                return render(request,'admin_profile.html',{'result':'Success'})
            else:
                obj = admindata.objects.filter(Email=email)
                obj1 = photodata.objects.filter(Email = email)
                return render(request,'admin_profile.html',{'data':obj,'Email':email,'data1':obj1})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def operator_profile(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method == 'POST'):
                return render(request,'operator_profile.html',{'result':'Success'})
            else:
                obj = operator.objects.filter(Email=email)
                obj1 = photodata.objects.filter(Email = email)
                return render(request,'operator_profile.html',{'data':obj,'Email':email,'data1':obj1})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def upload_photo_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                try:
                    upload_file=request.FILES['F1']
                    path = os.path.basename(upload_file.name)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) +'.'+ file_ext
                    fs = FileSystemStorage()
                    fs.save(filename,upload_file)
                    obj = photodata()
                    obj.Email = email
                    obj.Photo = filename
                    obj.save()
                    return render(request,'upload_photo_admin.html',{'result':'Success'})
                except:
                    return render(request,'upload_photo_admin.html',{'result':"Select Photo"})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def upload_photo_student_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                try:
                    email = request.POST['H1']
                    upload_file=request.FILES['F1']
                    path = os.path.basename(upload_file.name)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) +'.'+ file_ext
                    fs = FileSystemStorage()
                    fs.save(filename,upload_file)
                    obj = photodata()
                    obj.Email = email
                    obj.Photo = filename
                    obj.save()
                    return render(request,'upload_photo_student_admin.html',{'data':'Success'})
                except:
                    return render(request,'upload_photo_student_admin.html',{'result':"Select Photo"})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def upload_photo_student_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method == "POST"):
                try:
                    email = request.POST["H1"]
                    upload_file=request.FILES['F1']
                    path = os.path.basename(upload_file.name)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) +'.'+ file_ext
                    fs = FileSystemStorage()
                    fs.save(filename,upload_file)
                    obj = photodata()
                    obj.Email = email
                    obj.Photo = filename
                    obj.save()
                    return render(request,'upload_photo_student_operator.html',{'result':'Success'})
                except:
                    return render(request,'upload_photo_student_operator.html',{'result':"Select Photo"})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def view_operator_admin(request):
    if(request.session.has_key('usertype')):
        usertype= request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                email = request.POST["H1"]
                obj = operator.objects.filter(Email = email)
                obj1 = photodata.objects.filter(Email = email)
                return render(request,'view_operator_admin.html',{'key1':obj,'data1':obj1,'Email':email})
            else:
                return render(request,'view_operator_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def student_profile(request):
    if (request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if (usertype == 'student'):
            if (request.method == "POST"):
                return render(request, 'student_profile.html',{'result':"Success"})

            else:
                obj = student.objects.filter(Email=email)
                obj1 = photodata.objects.filter(Email=email)
                obj2 = st_course.objects.filter(email=email)

                student_course = []
                total_paid = 0
                for d in obj2:
                    paid = course_total(d.st_course_id)
                    total_paid = total_paid + paid
                    fees = d.fees
                    due = int(fees) - paid
                    aa = [d.st_course_id, d.course_id, d.email, d.course_name, d.fees, d.duration, d.commencement_date,
                          paid, due]
                    student_course.append(aa)

                    obj3 = st_installment.objects.filter(email=email)
                    t1 = all_course_fees(email)
                    total_due = t1 - total_paid
                return render(request, 'student_profile.html',{'data': obj, 'data1': obj1, 'data2': student_course, 'data3': obj3, 'total': t1,'total_paid': total_paid, 'total_due': total_due, 'email': email})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def upload_photo_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method == "POST"):
                try:
                    upload_file=request.FILES['F1']
                    path = os.path.basename(upload_file.name)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) +'.'+ file_ext
                    fs = FileSystemStorage()
                    fs.save(filename,upload_file)
                    obj = photodata()
                    obj.Email = email
                    obj.Photo = filename
                    obj.save()
                    return render(request,'upload_photo_operator.html',{'result':'Success'})
                except:
                    return render(request,'upload_photo_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def change_photo_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            obj = photodata.objects.get(Email = email)
            obj.delete()

            return render(request,'change_photo_admin.html',{'data':"Success"})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def change_photo_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']

        if(usertype == 'operator'):
            obj = photodata.objects.get(Email = email)
            obj.delete()
            return render(request,'change_photo_operator.html',{'data':'Success'})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def view_student_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                email = request.POST['H1']
                obj = student.objects.filter(Email=email)
                obj1 = photodata.objects.filter(Email=email)
                obj2 = st_course.objects.filter(email=email)

                student_course = []
                total_paid = 0
                for d in obj2:
                    paid = course_total(d.st_course_id)
                    total_paid = total_paid + paid
                    fees = d.fees
                    due = int(fees) - paid
                    aa = [d.st_course_id, d.course_id, d.email, d.course_name, d.fees, d.duration, d.commencement_date,
                          paid, due]
                    student_course.append(aa)

                obj3 = st_installment.objects.filter(email=email)
                t1 = all_course_fees(email)
                total_due = t1 - total_paid
                return render(request, 'view_student_admin.html',{'data': obj, 'data1': obj1, 'data2': student_course, 'data3': obj3, 'total': t1,'total_paid': total_paid, 'total_due': total_due, 'email': email})

            else:
                email = request.POST['H1']
                obj = student.objects.filter(Email=email)
                obj1 = photodata.objects.filter(Email=email)
                obj2 = st_course.objects.filter(email=email)

                student_course = []
                total_paid = 0
                for d in obj2:
                    paid = course_total(d.st_course_id)
                    total_paid = total_paid + paid
                    fees = d.fees
                    due = int(fees) - paid
                    aa = [d.st_course_id, d.course_id, d.email, d.course_name, d.fees, d.duration, d.commencement_date,
                          paid, due]
                    student_course.append(aa)

                obj3 = st_installment.objects.filter(email=email)
                t1 = all_course_fees(email)
                total_due = t1 - total_paid
                return render(request, 'view_student_admin.html',
                              {'data': obj, 'data1': obj1, 'data2': student_course, 'data3': obj3, 'total': t1,
                               'total_paid': total_paid, 'total_due': total_due, 'email': email})

                return render(request,'view_student_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def all_course_fees(email):
    obj=st_course.objects.filter(email = email)
    t=0
    for d in obj:
        t=t+ int(d.fees)
    return t

def course_total(cid):
    obj = st_installment.objects.filter(course_id = cid)
    t = 0
    for d in obj:
        t= t+int(d.amount)
    return t

def change_photo_student_admin(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method=="POST"):
                email = request.POST["H1"]
                obj = photodata.objects.get(Email = email)
                obj.delete()
                return render(request,'change_photo_student_admin.html',{'data':"Success"})
            else:
                return render(request,'change_photo_student_admin.html'  )
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def change_photo_student_operator(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'operator'):
            if(request.method=="POST"):
                email = request.POST["H1"]
                obj = photodata.objects.get(Email = email)
                obj.delete()
            else:
                return render(request,'change_photo_student_operator.html',{'data':"Photo Deleted"})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def view_student_operator(request):
    if (request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if (usertype == 'operator'):
            if (request.method == "POST"):
                email = request.POST['H1']
                obj = student.objects.filter(Email=email)
                obj1 = photodata.objects.filter(Email=email)
                obj2 = st_course.objects.filter(email=email)

                student_course = []
                total_paid = 0
                for d in obj2:
                    paid = course_total(d.st_course_id)
                    total_paid = total_paid + paid
                    fees = d.fees
                    due = int(fees) - paid
                    aa = [d.st_course_id, d.course_id, d.email, d.course_name, d.fees, d.duration, d.commencement_date,
                          paid, due]
                    student_course.append(aa)

                obj3 = st_installment.objects.filter(email=email)
                t1 = all_course_fees(email)
                total_due = t1 - total_paid
                return render(request, 'view_student_operator.html',
                              {'data': obj, 'data1': obj1, 'data2': student_course, 'data3': obj3, 'total': t1,'total_paid': total_paid, 'total_due': total_due, 'email': email})
            else:
                return render(request, 'view_student_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def course_reg(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            obj = course_master()
            if(request.method=="POST"):
                a = request.POST['T1']
                b = request.POST['T2']
                c = request.POST['T3']

                obj.course_name = a
                obj.fees = b
                obj.duration = c

                obj.save()
                return render(request,'course_reg.html',{'data':"Course Add"})
            else:
                return render(request,'course_reg.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def show_courses(request):
    if (request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if (usertype == 'admin'):
            obj = course_master.objects.all()

            return render(request,'show_courses.html',{'data':obj})
        else:
            return render(request,'show_courses.html')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_courses(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == "admin"):
            if(request.method == "POST"):
                course_id = request.POST['H1']
                obj = course_master.objects.filter(course_id=course_id)

                return render(request,'edit_courses.html',{'data':obj})
            else:
                return render(request,'edit_courses.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_courses_1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                course_id = request.POST['H1']
                obj = course_master.objects.get(course_id=course_id)
                a = request.POST['T1']
                b = request.POST['T2']
                c = request.POST['T3']

                obj.course_name = a
                obj.fees = b
                obj.duration = c

                obj.save()
                return render(request,'edit_courses_1.html',{'name':'Data changes'})
            else:
                return render(request,'edit_courses_1.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_courses(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                course_id = request.POST["H1"]
                obj = course_master.objects.filter(course_id=course_id)

                return render(request,'delete_courses.html',{'data':obj})
            else:
                return render(request,'delete_courses.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_courses_1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == "admin"):
            if(request.method == "POST"):
                course_id = request.POST['H1']

                obj = course_master.objects.get(course_id=course_id)

                obj.delete()
                return render(request,'delete_courses_1.html',{'name':'Course Deleted'})
            else:
                return render(request,'delete_courses_1.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def add_courses(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        email = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == 'POST'):
                email = request.POST['H1']
                obj = course_master.objects.all()
                return render(request,'add_courses.html',{'data':obj,'email':email})
            else:
                return render(request,'add_courses.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def add_courses_1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        e1 = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                email = request.POST['H1']
                course_id = request.POST['H2']
                obj = course_master.objects.get(course_id=course_id)
                obj1 = st_course()
                obj1.course_id = course_id
                obj1.email = email
                obj1.course_name = obj.course_name
                obj1.fees = obj.fees
                obj1.duration = obj.duration
                obj1.commencement_date = date.today()
                obj1.save()
                return render(request,'add_courses_1.html',{'name':"Continue"})
            else:
                return render(request,'add_courses_1.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def pay_installment(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        e1 = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                email = request.POST['H1']
                st_course_id = request.POST['H2']
                obj = st_course.objects.filter(email = email,st_course_id = st_course_id)
                return render(request,'pay_installment.html',{'data':obj})
            else:
                return render(request,'pay_installment.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def pay_installment_1(request):
    if(request.session.has_key('usertype')):
        usertype = request.session['usertype']
        e1 = request.session['Email']
        if(usertype == 'admin'):
            if(request.method == "POST"):
                email = request.POST['H1']
                st_course_id =request.POST['H2']
                obj = st_course.objects.filter(st_course_id=st_course_id)
                obj1 = st_installment(email = email)
                obj1.course_id = st_course_id
                obj1.amount = request.POST["T1"]
                obj1.t_date = date.today()
                obj1.remark = request.POST['T2']
                obj1.save()
                return render(request,'pay_installment_1.html',{'name':'Payment received Successfully'})
            else:
                return render(request,'pay_installment_1.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')
