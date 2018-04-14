from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(),name='school_list'),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='school_detail'),
    url(r'^create/$',views.SchoolCreateView.as_view(),name='school_create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='school_update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='school_delete'),
    url(r'^school/(?P<pk>\d+)/studentlist/$',views.StudentListView.as_view(),name='student_list'),
    url(r'^school/(?P<pk>\d+)/student/(?P<student_pk>\d+)/$',views.StudentDetailView.as_view(),name='student_detail'),
    url(r'^school/(?P<pk>\d+)/create/$',views.StudentCreateView.as_view(),name='student_create'),
    url(r'^school/(?P<pk>\d+)/update/(?P<student_pk>\d+)/$',views.StudentUpdateView.as_view(),name='student_update'),
    url(r'^school/(?P<pk>\d+)/delete/(?P<student_pk>\d+)/$',views.StudentDeleteView.as_view(),name='student_delete'),
    # url(r'^$',views.StudentListView.as_view(),name='student_list'),
    # url(r'^(?P<pk>\d+)/$',views.StudentDetailView.as_view(),name='student_detail'),
    # url(r'^create/$',views.StudentCreateView.as_view(),name='student_create'),
    # url(r'^update/(?P<pk>\d+)/$',views.StudentUpdateView.as_view(),name='student_update'),
    # url(r'^delete/(?P<pk>\d+)/$',views.StudentDeleteView.as_view(),name='student_delete')
]
# or url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),
#[-\w] means either a word character (A-Z a-z 0-9 _) or a dash (-) can go there
