from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import ChangeBalanceForm, PeriodForm
from .models import ChangeBalance, Period


# Данная вьюха отвечает за отображение созданных периодов
def period(request):
    if Period.objects.all().count() > 0:
        periods = Period.objects.all()
        return render(request, 'period.html', {'periods': periods})
    # Периоды не созданы, перенаправляем пользовател на страницу создания периода
    return redirect('/create_period')


# Представление для создания периода
def create_period(request):
    # Если пользовательввел данные в форму (и они передались в запросе методом POST), то
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        # 1. проверяем валидность данных
        if form.is_valid():
            # 2. записываем ввеенные данные в БД
            form.save()
            # 3. перенапрявляем пользователя на страницу выбора периодов
            return redirect('/period')
    else:
        # Если форма еще не заполнена, или пользователь только попал на страницу, то создаем и отображаем пустую форму
        form = PeriodForm()
        return render(request, 'create_period.html', {'form': form})


# Представление для обработки изменений бюджета
# реализован функционал создания/редактирования и удаления записей
# Весь функционал реализован в 1 представлении для следования принципу DRY Django, и для удобства рендеринга 1 формы.
# Возможно, стоило реализовать представление классом, но из-за отсутствия времени, не стал разбираться в данном вопросе.
# Функция, помимо запроса, принимает параметр со значением id периода, а также может принимать
# 2 необязательных параметра (по-умолчанию None): id записи для редактирования, id записи для удаления.
def changes(request, period_id, change_id=None, del_id=None):
    # Получаем запись из моели Period по принятому id
    period = Period.objects.get(id=period_id)
    # Получаем все записи таблицы Изменений, относящиеся к данному периоду
    table = ChangeBalance.objects.filter(period=period)
    # Получаем сумму по полю "сумма" во всех записях таблицы Изменений
    total = table.aggregate(Sum('sum'))

    if request.method == 'POST':
        form = ChangeBalanceForm(request.POST)
        if form.is_valid():
            # Получаем "очищенные" данные в виде словаря Python
            data = form.cleaned_data
            # Создаем запись, заносим данные и сохраняем запись
            change_balance = ChangeBalance()
            change_balance.period = period
            change_balance.date = data['date']
            # Если тип изменения "Расход" то в поле суммы записывается отрицательное число,
            # если "Поступление" - положительное.
            change_balance.sum = data['sum'] if data['change'] == 'Поступление' else -data['sum']
            change_balance.name = data['name']
            change_balance.category = data['category']
            change_balance.change = data['change']
            change_balance.save()
            # Перенаправляем пользователя на эту же страницу, тем самым получаем запрос к этой же функции методом GET.
            # В итоге пользователь видит форму на странице без данных.
            return redirect('/changes/' + period_id)
    else:
        # Если функция получила параметр change_id
        if change_id:
            # получаем данные из записи по полученному id
            try:
                change = ChangeBalance.objects.get(id=change_id)
            except:
                return redirect('/changes/' + period_id)
            data = {
                'date': change.date,
                'sum': abs(change.sum),
                'name': change.name,
                'category': change.category,
                'change': change.change
            }
            # создаем форму с заполненными данными для отображения на странице
            form = ChangeBalanceForm(initial=data)
            # удаляем запись с полученным id
            # Важно отметить, что здесь необходима оптимизация данного функционала, поскольку если пользователь
            # отправит запрос на редактирование, затем удалиться запись, и пользователю отобразиться страница,
            # с заполненной формой, а он данные не сохранит, то запись потеряется.
            # Проще говоря, по факту происходит не редактирование записи, а удаление старой и создание новой.
            change.delete()
        # Если функция получила параметр del_id
        elif del_id:
            # удаляем запись из таблицы по полученному id
            ChangeBalance.objects.get(id=del_id).delete()
            # перенаправляем пользователя на эту же страницу
            return redirect('/changes/' + period_id)
        else:
            # Если запрос к функции прошел методом GET и без параметров change_id и del_id, то создаем пустую форму.
            form = ChangeBalanceForm()
    # Заносим в словарь context все данные для отправки шаблонизатору
    context = {
        'period': period,
        'form': form,
        'table': table,
        'total': total['sum__sum']
    }
    # Отображаем страницу с необходимыми данными.
    return render(request, 'changes.html', context)
