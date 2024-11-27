"""
    This file creates the views for the property app.

    ''Views'': 
        PropertyList: - Display a list of properties using the Property Model.
        property_detail: - Display an individual property.
"""
from django.views import generic
from django.db.models import Q
from .models import Property


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

