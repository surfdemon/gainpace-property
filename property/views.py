"""
    This file creates the views for the property app.

    ''Views'': 
        PropertyList: - Display a list of properties using the Property Model.
        property_detail: - Display an individual property.
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.files.storage import DefaultStorage
from django.db.models import Q
from django.utils.text import slugify
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from formtools.wizard.views import SessionWizardView
from .models import Property
from .forms import PropertyForm, PropertyImageForm


# Create your views here.
class PropertyList(generic.ListView):
    """
        Display a list of properties using the Property Model.
        Based on the user's authentication status and property status.
    """
    queryset = Property.objects.filter(status=1)
    template_name = 'property/index.html'
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Property.objects.filter(
                Q(status=1) | Q(status=0, owner=user)
            )
        else:
            return Property.objects.filter(status=1)


def property_detail(request, slug):
    """
        Display an individual :model: property.
    """
    user = request.user
    if user.is_authenticated:
        queryset = Property.objects.filter(
            Q(status=1) | Q(status=0, owner=user)
        )
    else:
        queryset = Property.objects.filter(status=1)

    property_item = get_object_or_404(queryset, slug=slug)
    context = {"property": property_item, "images": property_item.images.all()}
    return render(request, 'property/detail.html', context)


class PropertyWizard(LoginRequiredMixin, SessionWizardView):
    """
        Display a form to create a new :model: property.
    """
    file_storage = DefaultStorage()
    form_list = [PropertyForm, PropertyImageForm]
    template_name = 'property/new.html'

    def done(self, form_list, **kwargs):
        property_form = form_list[0].save(commit=False)
        property_form.owner_id = self.request.user.id
        property_form.save()
        images_form = form_list[1].save(commit=False)
        images_form.property = property_form
        images_form.save()
        messages.success(self.request, 'Property added successfully')
        return HttpResponseRedirect(reverse('property_detail', args=[property_form.slug]))
