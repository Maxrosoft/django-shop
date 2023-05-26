from django.db import models
from django.urls import reverse

class Shop(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_shop', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'shop'
        verbose_name_plural = 'shops'

    def __str__(self):
        return self.name

class Product(models.Model):
    shop = models.ForeignKey(Shop,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name