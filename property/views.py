"""
    This file creates the views for the property app.

    ''Views'': 
        PropertyList: - Display a list of properties using the Property Model.
        property_detail: - Display an individual property.
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.core.files.storage import DefaultStorage
from django.db.models import Q
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from formtools.wizard.views import SessionWizardView
from .models import Property, PropertyImage
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


class EditProperty(UpdateView):
    """
        Display a form to edit an existing :model:'property.property'.
    """
    model = Property
    form_class = PropertyForm
    template_name = 'property/edit.html'
    context_object_name = 'property'

    def get_queryset(self):
        user = self.request.user
        return Property.objects.filter(owner=user)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(f"{form.instance.title}-{form.instance.id}")
        messages.success(self.request, 'Property updated successfully')
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class AddImage(generic.CreateView):
    model = PropertyImage
    form_class = PropertyImageForm
    template_name = 'property/add_image.html'
    context_object_name = 'property_image'

    def form_valid(self, form):
        property_to_update = get_object_or_404(Property, slug=self.kwargs['slug'])
        form.instance.property = property_to_update
        messages.success(self.request, 'Image added successfully')
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.property.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property'] = get_object_or_404(Property, slug=self.kwargs['slug'])
        return context
    