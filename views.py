from django.shortcuts import render
from .forms import CompanyForm

from django.utils import timezone

def company_new(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            Education = form.save(commit=False)
            # Education.userID = request.user
            Education.created_date = timezone.now()
            Education.save()
    else:
        form= CompanyForm()


# Create your views here.
