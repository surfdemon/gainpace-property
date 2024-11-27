from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


FURNISHED = ((0, "Either"), (1, "Furnished"), (2, "Unfurnished"))
STATUS = ((0, "Draft"), (1, "Publish"))


# Create your models here.
class Property (models.Model):
    """
    Model to store property details.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    ref = models.CharField(max_length=5)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="properties"
        )
    rent = models.FloatField()
    min_tenancy = models.IntegerField()
    max_tenancy = models.IntegerField()
    deposit = models.FloatField()
    ad_link = models.CharField(max_length=200)
    g_form = models.CharField(max_length=200)
    description = models.TextField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    max_tenants = models.IntegerField()
    bills = models.BooleanField(default=False)
    broadband = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    families = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    furnished = models.IntegerField(choices=FURNISHED, default=0)
    epc = models.CharField(max_length=1)
    dss = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Meta class to set ordering and verbose name.
        """
        ordering = ['-created_on']
        verbose_name_plural = "Properties"

    def save(self, *args, **kwargs):
        """
        Override save method to create slug if not set.
        """
        super().save(*args, **kwargs)
        print(f"Property saved: {self.slug}")
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}")
            self.save(update_fields=['slug'])
            print(f"Slug created: {self.slug}")

    def __str__(self):
        """
        Return string for property using title field.
        """
        return f'{self.title}'

    def get_absolute_url(self):
        """
        Return absolute url for property detail.
        """
        return reverse('property_detail', args=[self.slug])


class PropertyImage(models.Model):
    """
    Model to store images for a property.
    """
    title = models.CharField(max_length=200)
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="images"
        )
    image = CloudinaryField('image')
    description = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        """
        Meta class to set ordering and verbose name.
        """
        ordering = ['created_on']
        verbose_name = "Property Image"
        verbose_name_plural = "Property Images"

    def __str__(self):
        """
            Return string for image using image and property fields.
        """
        return f'Image {self.image} for {self.property}'
