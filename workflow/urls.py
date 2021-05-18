from django.urls import path
from .views import WorkflowViewSet



urlpatterns = [
    path('workflow', WorkflowViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('workflow/<str:pk>', WorkflowViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    }))

]