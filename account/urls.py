from django.urls import path
from .import views
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('', views.getRoutes),
    path('token/', views.MytokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('register/',views.RegisterView.as_view(),name='register')
]