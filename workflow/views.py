from rest_framework import viewsets, status
from rest_framework.response import Response

from workflow.models import Workflow
from .serializers import WorkflowSerializer


class WorkflowViewSet(viewsets.ViewSet):
    def list(self, request):  # api/workflow
        workflow = Workflow.objects.all()
        serializer = WorkflowSerializer(workflow, many=True)
        return Response(serializer.data)

    def create(self, request):  # api/workflow
        serializer = WorkflowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # api/workflow/{str:uuid}
        pass

    def partial_update(self, request):
        pass

    def destroy(self, request):
        pass
