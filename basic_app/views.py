#from django.shortcuts import render
#from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#

# Pretty simple right?
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'
    #note in school_list.html i have for i in school_list
    # Example of making your own:
    # context_object_name = 'schools'
    model = models.School
    template_name = '/school_list.html'



class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    #if i dont specify context_object_name then the default will be school
    model = models.School
    template_name = 'basic_app/school_detail.html'




#CRUD= Create Retrieve Update Delete
class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School
    template_name = 'basic_app/school_form.html'
    # template_name = 'basic_app/school_create_form.html'


class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School
    template_name = 'basic_app/school_form.html'

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:school_list")
    template_name = 'basic_app/school_confirm_delete.html'
# reverse_lazy:we dont want it to be evaluated when running our .py file and wait until it is deleted successfully and called as a sucess

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

class StudentListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'
    #note in school_list.html i have for i in school_list
    # Example of making your own:
    # context_object_name = 'schools'
    model = models.Student
    template_name = 'basic_app/student_list.html'

#
class StudentDetailView(DetailView):
    context_object_name = 'student_details'
    #if i dont specify context_object_name then the default will be school
    model = models.Student
    template_name = 'basic_app/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context

    # def get_queryset(self):
    #     queryset = super(StudentDetailView, self).get_queryset()
    #     return queryset.filter(school=self.kwargs['pk'])

#CRUD= Create Retrieve Update Delete
class StudentCreateView(CreateView):
    fields = ("name","age","school")
    model = models.Student
    template_name = 'basic_app/student_form.html'



class StudentUpdateView(UpdateView):
    fields = ("name","age","school")
    model = models.Student
    template_name = 'basic_app/student_form.html'
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        student_alt = Student.objects.get(id=self.kwargs.get('student_pk', ''))
        context['student_alt'] = student_alt
        return context


class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy(":student_list")
    template_name = 'basic_app/student_confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        student_alt = Student.objects.get(id=self.kwargs.get('student_pk', ''))
        context['student_alt'] = student_alt
        return context


#
# class StudentDetailView(DetailView):
#     context_object_name = 'student_details'
#     #if i dont specify context_object_name then the default will be school
#     model = models.Student
#     template_name = 'basic_app/student_detail.html'
#
# #CRUD= Create Retrieve Update Delete
# class StudentCreateView(CreateView):
#     fields = ("name","age")
#     model = models.Student
#
#
# class StudentUpdateView(UpdateView):
#     fields = ("name","age","school")
#     model = models.Student
#
# class StudentDeleteView(DeleteView):
#     model = models.Student
#     success_url = reverse_lazy("basic_app:student_list")
