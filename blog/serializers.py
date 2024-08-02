from collections import UserDict
from logging import raiseExceptions
from rest_framework import serializers
from blog.models import AllBlog, User


class BlogSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model=AllBlog
    fields="__all__"

  def get_photo_url(self, obj):
    request = self.context.get('request')
    photo_url = obj.fingerprint.url
    return request.build_absolute_uri(photo_url)


class RegisterSerializer(serializers.ModelSerializer):
  class Meta: 
    model=User
    fields=["username", "email", "password"]

  def validate(self, data):
    if data["username"]:
      user=User.objects.filter(username=data["username"])
      if user.exists():
        raise serializers.ValidationError("Username already taken ")
    if data["email"]:
      user=User.objects.filter(email=data["email"])
      if user.exists():
        raise serializers.ValidationError("Email already exists!")

    return data


  def create(self, validated_data):
    user=User.objects.create(
      username=validated_data["username"],
      email=validated_data["email"]
    )
    user.set_password(validated_data["password"])
    user.save()
    return validated_data


class LoginSerializer(serializers.ModelSerializer):
  class Meta: 
    model=User
    fields=["username", "password"]
