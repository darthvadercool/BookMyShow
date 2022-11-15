from django.urls import path
from .views import CouponList, CouponDetail


urlpatterns = [
    path('coupon/', CouponList.as_view()),
    path('coupon/<int:pk>/', CouponDetail.as_view()),





]
