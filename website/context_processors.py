from .models import SocialNetWorks


def networks(request):
    return{
    'global_nrtworks':SocialNetWorks.objects.all
} 