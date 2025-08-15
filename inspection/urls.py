# inspection/urls.py
from django.urls import path
from .views import RegisterUser, LoginUser,TestAPi

urlpatterns = [
    path("registerUser/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("testAPi/", TestAPi.as_view(), name="testAPi"),
]
