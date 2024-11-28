from .models import Property, PropertyImage
from django import forms


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = (
            'title', 
            'ref', 
            # 'owner', - THis should be the person that is logged in!
            'rent', 
            'min_tenancy', 
            'max_tenancy', 
            'deposit', 
            'ad_link', 
            'g_form', 
            'description', 
            'bedrooms', 
            'bathrooms', 
            'max_tenants', 
            'bills', 
            'broadband', 
            'student', 
            'families', 
            'pets', 
            'smoking', 
            'garden', 
            'parking', 
            'furnished', 
            'epc', 
            'dss', 
            'featured',
            )

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields =  ('image', 'title', 'description', )

