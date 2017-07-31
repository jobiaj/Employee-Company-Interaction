from django.conf.urls import url
from relation import views

urlpatterns = [
    url(r'^$', views.get_homepage, name='index'),
    url(r'^outing/$', views.OutingPageView.as_view(), name='outing'),
    url(r'^team_list/$', views.TeamListView.as_view(), name='team_list'),
    url(r'^accounts/login/$', views.user_login, name='eci_login'),

]