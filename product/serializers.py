from rest_framework import serializers
from .models import Product
from user.models import User


class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
