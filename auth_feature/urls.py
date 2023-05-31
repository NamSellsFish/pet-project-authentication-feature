from django.urls import path
from .views import MySignUpView,MyPasswordResetView,MyPasswordResetConfirmView,MyLoginView
urlpatterns = [
    path("login/",MyLoginView.as_view(),name = 'login'),
    path("signup/", MySignUpView.as_view(), name='signup'),
    path("password_reset/", MyPasswordResetView.as_view(), name="password_reset"),
    path(
        "reset/<uidb64>/<token>/",
        MyPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]