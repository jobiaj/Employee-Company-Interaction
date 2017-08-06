from django.conf.urls import url
from relation.views import basics

urlpatterns = [
    url(r'^relation/homepage/$', basics.get_homepage, name='homepage'),
    url(r'^outing/$', basics.OutingPageView.as_view(), name='outing'),
    url(r'^team_list/$', basics.TeamListView.as_view(), name='team_list'),
    url(r'^accounts/login/$', basics.user_login, name='eci_login'),
    url(r'^accounts/logout/$', basics.user_logout, name='eci_logout'),
    url(r'^relation/userprofile/$',basics.get_userprofile,name='get_userprofile'),
    url(r'^$', basics.get_homepage, name='homepage'),

]