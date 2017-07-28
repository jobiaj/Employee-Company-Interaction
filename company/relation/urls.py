from django.conf.urls import url
from relation import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^$', views.OutingPageView.as_view(), name='outing')
]