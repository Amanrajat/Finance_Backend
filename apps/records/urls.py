from django.urls import path
from .views import RecordListCreateView, RecordDetailView

urlpatterns = [
    path('', RecordListCreateView.as_view()),
    path('<uuid:pk>/', RecordDetailView.as_view()),
]