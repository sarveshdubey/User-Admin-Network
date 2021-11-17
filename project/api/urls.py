from django.urls import path
from .views import AdminView,UserRegisterView,UserLoginView

urlpatterns = [
    
    path('advisor',AdminView.as_view()),
    path('register',UserRegisterView.as_view()),
    path('login',UserLoginView.as_view()),
]