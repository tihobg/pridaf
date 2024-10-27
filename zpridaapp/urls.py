from django.urls import path
from . import views
from .views import register

urlpatterns = [

    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('logout/', views.logout_view, name='logout'),
    path('preeclampsia/', views.preeclampsia, name='preeclampsia'),
    path('pregnant_controls/', views.pregnant_controls, name='pregnant_controls'),
    path('spontaneous_abortions/', views.spontaneous_abortions, name='spontaneous_abortions'),
    path('database/', views.database, name='database'),
    path('news/', views.news, name='news'),
    path('users/register/', views.register, name='register'),
    path('users/login/', views.login_view, name='login'),
    path('users/correlation', views.correlation, name='correlation'),
    # path('login/', views.login, name='login'),
    # path('home/', views.home, name='home'),

    path('home1/', views.home1, name='home1'),
    path('add_edit_patient', views.add_edit_patient, name='add_edit_patient'),
    path('base/', views.base, name='base'),
    # path('users/correlation/', views.correlation, name='correlation'),

]