from django.db import models

# Create your models here.
class teacher_details(models.Model):
    Teacher_name=models.CharField(max_length=255)
    def __str__(self):
        return self.Teacher_name

class coursename(models.Model):
    Course=models.CharField(max_length=255)
    fee=models.IntegerField()
    def __str__(self):
        return self.Course
        
class student_details(models.Model):
    Stud_name=models.CharField(max_length=255)
    Course=models.ForeignKey(coursename,on_delete=models.CASCADE,null=True) 
    TName=models.ForeignKey(teacher_details,on_delete=models.CASCADE,null=True)
    Place=models.CharField(max_length=255)
    stud_age=models.IntegerField()
    def __str__(self):
        return self.Stud_name

