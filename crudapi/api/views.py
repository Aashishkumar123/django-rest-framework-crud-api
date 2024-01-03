from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from ..models import Student
from .serializers import StudentSerializer


class StudentAPIView(APIView):
    def get_queryset(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "Invalid Student ID!",
                }
            )

    def get(self, request, id=None):
        if id is None:
            students = Student.objects.all()
            student_serializer = StudentSerializer(students, many=True)
        else:
            student_serializer = StudentSerializer(self.get_queryset(id=id))
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Success",
            "data": student_serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_data = student_serializer.save()
            response = {
                "status_code": status.HTTP_201_CREATED,
                "message": "Student created!",
                "data": StudentSerializer(student_data).data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": "bad request",
                "errors": student_serializer.errors,
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        student_serializer = StudentSerializer(
            instance=self.get_queryset(id=id), data=request.data, partial=True
        )
        if student_serializer.is_valid():
            updated_student_data = student_serializer.save()
            response = {
                "status_code": status.HTTP_201_CREATED,
                "message": "Student updated!",
                "data": StudentSerializer(updated_student_data).data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": "bad request",
                "errors": student_serializer.errors,
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        self.get_queryset(id=id).delete()
        response = {
            "status_code": status.HTTP_201_CREATED,
            "message": "Student deleted!",
        }
        return Response(response, status=status.HTTP_201_CREATED)
