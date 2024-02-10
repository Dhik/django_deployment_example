from django.urls import path
from first_app import views

app_name = 'basic_app'
urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.users, name="users"),
    path('formpage/', views.form_name_view, name="forms"),
    path('register/', views.register, name="register"),

    path('rel_url/', views.index_rel_url, name="rel_url"),
    path('relative/', views.relative, name="relative"),
    path('other/', views.other, name="other"),
]
