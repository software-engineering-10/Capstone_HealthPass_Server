from rest_framework import serializers
from .models import Account
from .models import Reservation

class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name','phone','email','password']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['day','time','minute','email','seat','ex_name','user_name','user_phone']