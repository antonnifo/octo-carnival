from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from  rest_framework.permissions import IsAuthenticated

from .models import UserProfile, ProfileFeedItem
from .serializers import UserProfileSerializer, ProfileFeedItemSerializer
from .permissions import UpdateOwnProfile, UpdateOwnStatus

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = UserProfileSerializer
    queryset         = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes     = (UpdateOwnProfile, IsAuthenticated)
    filter_backends  = (filters.SearchFilter,)
    search_fields    = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating,Reading, Deleting and updating of profile feed items"""

    authentication_classes = (TokenAuthentication, )
    serializer_class       = ProfileFeedItemSerializer
    queryset               = ProfileFeedItem.objects.all()
    permission_classes     = (
        UpdateOwnStatus, IsAuthenticated
    )

    def perform_create(self,serializer):
        """sets user profile to the logged in user"""

        serializer.save(user_profile=self.request.user)
    

      
