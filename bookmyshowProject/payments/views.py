from rest_framework import generics

from .serializers import CouponDetailSerializer, CouponListSerializer
from .models import Coupon


class CouponList(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponListSerializer


class CouponDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponDetailSerializer
