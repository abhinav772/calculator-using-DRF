from django.urls import path

from operation.api.views import AddResult, SubtractResult, MultiplyResult, DivideResult

urlpatterns = [
    path('anum/', AddResult.as_view(), name='add'),
    path('snum/', SubtractResult.as_view(), name='subtract'),
    path('mnum/', MultiplyResult.as_view(), name='multiply'),
    path('dnum/', DivideResult.as_view(), name='divide')
]