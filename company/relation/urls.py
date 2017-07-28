from django.conf.urls import url
from relation import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^outing/$', views.OutingPageView.as_view(), name='outing'),
    url(r'^team_list/$', views.TeamListView.as_view(), name='team_list')
]