from django.shortcuts import HttpResponse
from rest_framework import serializers, status, generics
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

        def post(self, request):
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)