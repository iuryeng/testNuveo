
from django.urls import path

from . import views
from .views import WorkflowViewSet

urlpatterns = [
    path('workflow', WorkflowViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('workflow/<str:pk>', WorkflowViewSet.as_view({
        'patch': 'partial_update',
    })),
    path('workflow/consume/<str:pk>', WorkflowViewSet.as_view({
        'get': 'workflow_consume',
    })),

 ]