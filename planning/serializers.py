from rest_framework import serializers
from .models import Period, ChangeBalance


class PeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'name', 'start_day', 'end_day')


class ChangeBalanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChangeBalance
        fields = '__all__'
