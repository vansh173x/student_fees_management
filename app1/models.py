from django.db import models

# Create your models here.

class admindata(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Email = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Name

class login(models.Model):
    Email = models.CharField(max_length=100,primary_key=True)
    Password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

    def __str__(self):
        return self.Email

class operator(models.Model):
    Name = models.CharField(max_length=100)
    Address =models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Email = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Name
class student(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Email = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Name

class photodata(models.Model):
    Email = models.CharField(max_length=100,primary_key=True)
    Photo = models.CharField(max_length=100)

    def __str__(self):
        return self.Photo

class course_master(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    fees = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class st_course(models.Model):
    st_course_id = models.AutoField(primary_key=True)
    course_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    fees = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    commencement_date = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class st_installment(models.Model):
    t_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    t_date = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)

    def __str__(self):
        return self.email