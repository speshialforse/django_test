from django.urls import path
from tutorials_view import views
 
urlpatterns = [ 
    path('tutorials_view/members', views.tutorials_view, name="tutorials_view"),
]