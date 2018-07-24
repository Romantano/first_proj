from rest_framework import serializers
from .models import Period, ChangeBalance

# Сериализатор для получения периодов
class PeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'name', 'start_day', 'end_day')

# Сериализатор для получения  изменений
class ChangeBalanceSerializers(serializers.ModelSerializer):
    period = PeriodSerializers()

    class Meta:
        model = ChangeBalance
        fields = '__all__'
