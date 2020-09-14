from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DispatchView

dispatch_list = DispatchView.as_view({
    'post': 'create',
    'get': 'list'
})

dispatch_detail = DispatchView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'pathch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('dispatches/', dispatch_list, name='dispatch_list'),
    path('dispatches/<int:pk>/', dispatch_detail, name='dispatch_detail'),
])
