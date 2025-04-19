from django.db import models
from django.utils import timezone
# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='banner/', default='')
    text=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True, verbose_name="Активен" )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"    

class SocialNetWorks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image=models.ImageField(upload_to='networks',default='')
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Социальная сеть"

class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(max_length=255)
    image=models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Новость"
        ordering = ['-created_at']
        