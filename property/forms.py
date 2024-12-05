from .models import Property, PropertyImage
from django_summernote.widgets import SummernoteWidget
from django import forms


class PropertyForm(forms.ModelForm):
    """
    Form to create a new property.
    """

    class Meta:
        model = Property
        fields = (
            "title",
            "ref",
            "rent",
            "min_tenancy",
            "max_tenancy",
            "deposit",
            "ad_link",
            "g_form",
            "description",
            "bedrooms",
            "bathrooms",
            "max_tenants",
            "bills",
            "broadband",
            "student",
            "families",
            "pets",
            "smoking",
            "garden",
            "parking",
            "furnished",
            "epc",
            "dss",
            "featured",
        )
        widgets = {
            "description": SummernoteWidget(),
        }


class PropertyImageForm(forms.ModelForm):
    """
    Form to add images to a property.
    """

    class Meta:
        model = PropertyImage
        fields = (
            "image",
            "title",
            "description",
        )
