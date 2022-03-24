from django.forms import modelformset_factory
from django.shortcuts import render

from geeksforgeeks.models import GeeksModel


def formset_view(request):
    context = {}

    # creating a formset
    GeeksFormSet = modelformset_factory(GeeksModel, fields=('title', 'description'), extra=3)
    formset = GeeksFormSet(request.POST or None)

    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, "geeksforgeeks/home.html", context)
