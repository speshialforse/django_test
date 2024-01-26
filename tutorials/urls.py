from django.urls import re_path, path
from tutorials import views
 
urlpatterns = [ 
    path('api/tutorials', views.tutorial_list, name="tutorials"),
    # re_path(r'^api/tutorials$', views.tutorial_list),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path(r'^api/tutorials/published$', views.tutorial_list_published),
    path('view/members', views.members, name="members"),
    path('api/testjson', views.testjson, name="testjson"),
]