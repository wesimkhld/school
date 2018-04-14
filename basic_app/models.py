from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse
#from django.shortcuts import redirect

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)
        #return str(self.id)
        #return str(self.pk)

    def get_absolute_url(self):
        return reverse("basic_app:school_detail",kwargs={'pk':self.pk})
        #return redirect("basic_app:detail",kwargs={'pk':self.pk})
        #return redirect does NOT work

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("basic_app:student_detail",kwargs={'pk':self.pk})
