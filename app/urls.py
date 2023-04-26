from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet, StudentView

from . import views

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('students/', StudentView.as_view()),
    # path('viewset/students/<int:pk>/', views.StudentViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}
]