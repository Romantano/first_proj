import datetime
from dateutil.relativedelta import relativedelta
from django.db import models


# Модель Периода
class Period(models.Model):
    name = models.CharField('Название периода', max_length=30, blank=False)
    # Поле описание так нигде и не использовалось. Пусть будет)))
    description = models.TextField('Описание периода', blank=True)
    # Начало периода по-умолчанию = текущая дата
    start_day = models.DateField('Начало периода', default=datetime.date.today)
    # Конец периода по-умолчанию = текущая дата + 1 месяц
    end_day = models.DateField('Конец периода', default=datetime.date.today() + relativedelta(months=+1))

    # Выполнена обратная сотрировка записей в модели
    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'
        ordering = ['start_day']

    def __str__(self):
        return self.name


# Модель внесения изменений в бюджет
class ChangeBalance(models.Model):
    # Привязываем изменения к периоду. При удалении периода, удаляются все изменения относящиеся к данному периоду.
    period = models.ForeignKey(Period, verbose_name='Период', on_delete=models.CASCADE, default=None)
    date = models.DateField('Дата:', default=datetime.date.today)
    # Для работы с финансами, выбран тип Decimal с 2 знакам после запятой
    sum = models.DecimalField('Сумма:', decimal_places=2, max_digits=10)
    name = models.CharField('Название:', max_length=50, null=True)
    category = models.CharField('Категория:', max_length=50, null=True)
    choises_balans = (
        ('Расход', 'Расход'),
        ('Поступление', 'Поступление')
    )
    # Для занесения данных о типе изменения (дебет/кредит), применяется тип поля CharField c селектором.
    change = models.CharField(max_length=11, choices=choises_balans, default='Расход')

    class Meta:
        verbose_name = 'Изменение'
        verbose_name_plural = 'Изменения'
        ordering = ['date']

    def __str__(self):
        return str(self.sum)
