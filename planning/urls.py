from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'create_period/', views.create_period),
    url(r'period/', views.period),
    url(r'changes/(?P<period_id>\d+)/$', views.changes),
    url(r'changes/(?P<period_id>\d+)/(?P<change_id>\d+)/$', views.changes),
    url(r'changes/(?P<period_id>\d+)/del(?P<del_id>\d+)/$', views.changes),
]
