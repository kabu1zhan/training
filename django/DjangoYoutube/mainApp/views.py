from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TestForm
# Create your views here.
def index(request):
    return render(request, 'mainApp/html/homePage.html')

def contact(request):
    return render(request, 'mainApp/html/contacts.html', {'content': ["Я решала, если надо че то решить звоните сюда",
                                                                      "87786080445"]}
                  )
def testoviy_otziv(request, pk):
    proverka = get_object_or_404(OtzivInstance, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            proverka.save()

            return HttpResponseRedirect(reverse('all-borrowed'))