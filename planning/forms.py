from django import forms
from .models import ChangeBalance, Period


# Создаем формы на основе имеющихся моделей
class PeriodForm(forms.ModelForm):
    class Meta:
        # Привязываем модель к данной форме
        model = Period
        # Указываем необходимые поля и их порядок для отображения
        fields = ('name', 'start_day', 'end_day', 'description',)
        # Поля для ввода дат будут отображаться с использованием виджета
        widgets = {'start_day': forms.SelectDateWidget,
                   'end_day': forms.SelectDateWidget}


class ChangeBalanceForm(forms.ModelForm):
    class Meta:
        model = ChangeBalance
        fields = ('date', 'sum', 'name', 'category', 'change')
        widgets = {'date': forms.SelectDateWidget}
