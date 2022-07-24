from pickle import NEXT_BUFFER
from django.urls import path
from.views import *
from django.contrib.auth.views import LogoutView,PasswordChangeView,PasswordChangeDoneView
from.form import MyChangePasswordForm


urlpatterns = [
    path('', home,name='home' ),
    path('signup/', SignupView.as_view(),name='signup' ),
    path('login/', MyloginView.as_view(),name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout' ),
    path('change-password/',PasswordChangeView.as_view(template_name="core/change-password.html ",form_class=MyChangePasswordForm),name='change-password'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name="core\password-change-done.html"),name='password_change_done')
]
