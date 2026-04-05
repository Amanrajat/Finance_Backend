from django.urls import path
from .views import RegisterView, UpdateRoleView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('update-role/<uuid:user_id>/', UpdateRoleView.as_view()),
]