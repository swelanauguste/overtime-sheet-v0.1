from django.urls import path

from .views import OvertimeCreateView, OvertimeDetailView, OvertimeListView

urlpatterns = [
    path("", OvertimeListView.as_view(), name="ot-list"),
    path("add/", OvertimeCreateView.as_view(), name="ot-create"),
    path("detail/<int:pk>/", OvertimeDetailView.as_view(), name="ot-detail"),
]
