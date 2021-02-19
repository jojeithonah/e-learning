from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


router = DefaultRouter()



urlpatterns = [
    path('token-refresh/', TokenRefreshView.as_view()),
    path('token/', views.MyTokenObtainPairView.as_view()),
    path('register/', views.RegisterView.as_view()),
]

urlpatterns += router.urls
