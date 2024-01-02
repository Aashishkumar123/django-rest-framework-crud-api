from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path("students/", StudentAPIView.as_view(), name="student-api"),
    path("students/<int:id>/", StudentAPIView.as_view(), name="student-id-api"),
]
