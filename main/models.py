from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    is_best_seller = models.BooleanField(default=False)
    pet_friendly = models.BooleanField(default=True)
    
    # Pricing Tiers
    price_regular_current = models.DecimalField(max_digits=10, decimal_places=2)
    price_regular_srp = models.DecimalField(max_digits=10, decimal_places=2)
    price_deluxe_current = models.DecimalField(max_digits=10, decimal_places=2)
    price_deluxe_srp = models.DecimalField(max_digits=10, decimal_places=2)
    price_premium_current = models.DecimalField(max_digits=10, decimal_places=2)
    price_premium_srp = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Use help_text here to avoid the TypeError
    includes_list = models.TextField(help_text="Enter items separated by commas")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_includes_items(self):
        """Splits the comma-separated string into a list for the template."""
        if self.includes_list:
            return [item.strip() for item in self.includes_list.split(',')]
        return []

    def __str__(self):
        return self.name