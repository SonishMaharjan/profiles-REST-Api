
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to update their own profile"""

    #this function is called everytime when the request is made to api
    def has_object_permission(self,request,view,obj):
        """checks user is trying to edit own profiles"""

        #GET is a safe method
        if request.method in permissions.SAFE_METHODS:
            return True

        #if obj is same as user returns true else False
        return obj.id == request.user.id
