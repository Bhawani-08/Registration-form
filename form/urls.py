from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun1,name = 'fun1'),
    path('register',views.register,name = 'register'),
    path('registration_success/',views.registration_success,name = 'registration-success'),
    path('login/',views.login,name = 'login'),

    


]
