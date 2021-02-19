
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import ugettext as _
from rest_framework import serializers

from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


from . import models

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['permission'] = {
            'type': self.user.type,
            'type_name': self.user.get_type_display(),
        }
        
        return data


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = models.User
        fields = (
            'id',            
            'type',
            'full_name',
            'email',
            'username',
            'password',
            'is_active',
        )
        extra_kwargs = {
            'is_staff': {'read_only': True},
            'username': {'read_only': True},
            }


    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_email(self, value):
        value = value.lower()
        user = models.User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError(_('The email: %(value)s is already registered.') % {'value': value})
        return value

    def validate_password(self, value):
        request = self.context.get('request', None)
        confirm_password = request.data.get('confirm_password', None)

        if confirm_password != value:
            raise serializers.ValidationError(_('Passwords do not match.'))
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e)

        return value
