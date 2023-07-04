from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .models import Overtime


class OvertimeListView(ListView):
    model = Overtime


class OvertimeDetailView(DetailView):
    model = Overtime


class OvertimeCreateView(CreateView):
    model = Overtime
    fields = "__all__"
