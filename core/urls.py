from django.urls import path

from .views import *

urlpatterns = [
    path("transaction/<str:transaction_id>/",transactionViewSet.as_view(),name="transaction"),
    path("transactionSummaryByProducts/<str:last_n_days>/",transactionSummaryByProductsViewSet.as_view(),name="transactionSummaryByProducts"),
    path("transactionSummaryByManufacturingCity/<str:last_n_days>/",transactionSummaryByManufacturingCityViewSet.as_view(),name="transactionSummaryByManufacturingCity"),
]
