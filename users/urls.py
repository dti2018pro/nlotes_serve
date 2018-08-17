from django.urls import path
from . import views

urlpatterns = [
    path('xsignup/', views.SignUp.as_view(), name='signup'),
]
