from _testcapi import raise_exception

from rest_framework import viewsets, status
from rest_framework.response import Response

from workflow.models import Workflow
from .inserted import publish
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
        publish()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):  # api/workflow/{str:uuid}
        workflow = Workflow.objects.get(UUID=pk)
        serializer = WorkflowSerializer(instance=workflow, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def workflow_consome(self, request):
        pass
