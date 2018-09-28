from django.shortcuts import render, HttpResponseRedirect
from .models import Restaurant, MenuObj,OrderList
from .models import Option
# Create your views here.


def rest(request):
    r_list = Restaurant.objects.all()
    context = {'r_list': r_list}
    return render(request, 'order/rest.html', context)


def subway(request):
    r = Restaurant.objects.filter(name='subway')
    m_list = MenuObj.objects.filter(restaurant=r[0])
    context = {'m_list': m_list}
    return render(request, 'order/subway.html', context)


def submit_subway(request):
    if request.method == "POST":
        ol = OrderList()
        order_list = request.POST.get('options')
        s = ''
        for o in order_list:
            s += o
            s += '\n'
        ol.order = s
        ol.user = request.user
        ol.save()
        return HttpResponseRedirect('/order/subway_check')


def subway_check(request):
    ol = OrderList.objects.all()
    context = {'ol': ol}
    return render(request, 'order/subway_check.html', context)



