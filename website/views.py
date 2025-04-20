from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    all_achiev_cats = AchievCategory.objects.prefetch_related('category').all()
    active_achiev_cat = all_achiev_cats.first()
    
    return render(request, 'website/pages/index.html', {
        'banner': Banner.objects.filter(is_active=True).order_by('-created_at'),
        'news': News.objects.all(),
        'achiev_categories': all_achiev_cats,
        'active_achiev_cat': active_achiev_cat,
    })