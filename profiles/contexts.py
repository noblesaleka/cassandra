from django.shortcuts import get_object_or_404
from profiles.models import UserProfile


def membership_status(request):

    user =  request.user

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
    else:
        profile = ''

    context = {
        'profile': profile,
    }

    return context
