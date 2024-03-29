from django.db import models


class Student(models.Model):
    name = models.CharField(verbose_name="Student Name", max_length=100)
    email = models.EmailField(verbose_name="Student Email", max_length=277)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
