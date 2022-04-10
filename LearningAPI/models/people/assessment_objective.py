from django.db import models
from ..coursework import LearningObjective
from . import Assessment

class AssessmentObjective(models.Model):
    """Assessment objective model"""
    assessment = models.ForeignKey(
        Assessment, on_delete=models.CASCADE, related_name="objectives")
    objective = models.ForeignKey(
        LearningObjective, on_delete=models.CASCADE, related_name="assessments")
