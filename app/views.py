from rest_framework import viewsets
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from .models import Course, Student, Mentor
from .serializers import CourseSerializer, StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
