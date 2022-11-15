from rest_framework import serializers

from .models import Coupon, Payment


class CouponListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = ['id', 'name']


class CouponDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = ['id', 'name', 'discount', 'validtill']
