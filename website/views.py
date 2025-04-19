from django.shortcuts import render
from .models import Banner,News
# Create your views here.
def index(request):
    news=News.objects.all
    active_banner= Banner.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'website/pages/index.html',{'banner': active_banner,
                                                       'news':news})