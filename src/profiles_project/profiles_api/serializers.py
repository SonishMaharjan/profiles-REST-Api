
from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializing name field for testing our ApiView"""
    name = serializers.CharField(max_length= 10)

#serliazer that can be used with models
class UserProfileSerializer(serializers.ModelSerializer):
    """serializer for our user profile object"""

    #Meta class defines Django serializers to take what field from model
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')

        extra_kwargs= {'password':{"write_only":True}}
    #Overrides create function
    #all validated data are stored in validated_data
    def create(self,validated_data):
        """create new user"""
        user = models.UserProfile(
                email = validated_data['email'],
                name = validated_data["name"]
        )
        #changes password to hassh
        user.set_password(validated_data["password"])
        user.save()
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Profile Serializer for news feed item"""
    class Meta:
         model = models.ProfileFeedItem
         #user_profile takes id as it is foriegn Key
         #field must be list or tuple not dictionay
         fields= ('id','user_profile','status_text','created_on',)

         extra_kwargs= {"user_profile":{"read_only":True,},}
