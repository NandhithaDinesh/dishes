from rest_framework import serializers
from dishapp.models import Dishes
from django.contrib.auth.models import User

class DishSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()

    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid data")
        return data
class DishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        # fields=["name",
        #        "category",
        #         "price",
        #         "rating"]
        fields="__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)