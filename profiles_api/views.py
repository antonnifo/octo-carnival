from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.authentication import TokenAuthentication

from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import UpdateOwnProfile

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = UserProfileSerializer
    queryset         = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes     = (UpdateOwnProfile,)
    filter_backends  = (filters.SearchFilter,)
    search_fields    = ('name', 'email',)  
