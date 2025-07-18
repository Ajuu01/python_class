from django.db import models
from django.utils.text import slugify
# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(null=True,blank=True)#45 chars
    market_price=models.DecimalField(max_digits=10,decimal_places=2)
    actual_price=models.DecimalField(max_digits=10,decimal_places=2)
    short_description=models.CharField(max_length=100)
    description=models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)[:45]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return super().__str__(self)
    
