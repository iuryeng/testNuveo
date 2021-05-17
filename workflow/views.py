from rest_framework import viewsets


class WorkflowViewSet(viewsets.ViewSet):
    def list(self, request):  # api/workflow
        pass

    def create(self, request):  # api/workflow
        pass

    def retrieve(self, request, pk=None):  # api/workflow/{str:uuid}
        pass

    def partial_update(self, request):
        pass
