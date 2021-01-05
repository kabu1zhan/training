from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TestForm


def testoviy_otziv(request, pk):
    proverka = get_object_or_404(OtzivInstance, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            proverka.save()

            return HttpResponseRedirect(reverse('all-borrowed'))