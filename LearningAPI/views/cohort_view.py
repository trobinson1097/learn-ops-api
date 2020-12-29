from rest_framework import serializers
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAdminUser
from LearningAPI.models import Cohort, NssUser
from rest_framework.response import Response


class CohortViewSet(ViewSet):
    """Cohort view set"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized instance
        """
        student = NssUser.objects.get(user=request.auth.user)

        return Response({}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        return Response({}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """Handle PUT requests

        Returns:
            Response -- Empty body with 204 status code
        """
        return Response({}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single item

        Returns:
            Response -- 200, 404, or 500 status code
        """
        return Response({}, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        return Response({}, status=status.HTTP_200_OK)


class CohortSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = Cohort
        fields = '__all__'
