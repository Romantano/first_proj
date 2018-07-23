from django.http import JsonResponse
from .models import Period, ChangeBalance
from .serializers import PeriodSerializers, ChangeBalanceSerializers


def get_period(request):
    period = PeriodSerializers(
        Period.objects.all(),
        many = True
    ).data
    return JsonResponse({'period': period})
