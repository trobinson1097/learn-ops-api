"""Model for assessment statuses"""
from django.db import models


class StudentAssessmentStatus(models.Model):
    """Model for assessment statuses"""
    status = models.CharField(max_length=512)
