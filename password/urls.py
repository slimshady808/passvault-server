from django.urls import path
from .import views

urlpatterns = [
    path('', views.getRoutes),
    path('password/',views.PasswordCreateListView.as_view(),name='password-create-list'),
    path('password/<int:user_id>/',views.PasswordListByUserIDView.as_view(),name='password-list'),
    path('delete_password/<int:id>/',views.delete_password,name='delete-password')
]