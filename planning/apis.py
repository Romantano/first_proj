from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Period, ChangeBalance
from .serializers import PeriodSerializers, ChangeBalanceSerializers

# Описание представлений для выгрузги данных. Используется класс наследуемый от APIView
# для возможости получения данных в формате json и api


class GetPeriod(APIView):

    def get(self, request):
        period = Period.objects.all()
        serializer = PeriodSerializers(period, many=True)
        return Response(serializer.data)


class GetChanges(APIView):

    def get(self, request):
        changes = ChangeBalance.objects.all()
        serializer = ChangeBalanceSerializers(changes, many=True)
        return Response(serializer.data)
