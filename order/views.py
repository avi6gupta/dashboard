from django.shortcuts import render, HttpResponseRedirect
from .models import Restaurant, OrderList
from .models import Option
# Create your views here.


def rest(request):
    r_list = Restaurant.objects.all()
    context = {'r_list': r_list}
    return render(request, 'order/rest.html', context)


def name(request, foo):

    o_list = Option.objects.filter(restaurant__name=foo)
    context = {'o_list': o_list}
    return render(request, 'order/name.html', context)


# def subway(request):
#
#     o_list = Option.objects.filter(restaurant__name="Subway")
#     context = {'o_list': o_list}
#     return render(request, 'order/subway.html', context)
#
#
# def fw(request):
#
#     o_list = Option.objects.filter(restaurant__name="Florentine")
#     context = {'o_list': o_list}
#     return render(request, 'order/fw.html', context)
#
#
# def bnr(request):
#     # r = Restaurant.objects.filter(name.html='Baskin-Robbins')
#     o_list = Option.objects.filter(restaurant__name="Baskin-Robbins")
#     context = {'o_list': o_list}
#     return render(request, 'order/bnr.html', context)

def submit(request, foo):
    if request.method == "POST":
        ol = OrderList()
        order_list = request.POST.getlist('options')
        s = ''
        option_list = Option.objects.filter(option=order_list[0])
        ol.restaurant = option_list[0].restaurant
        for o in order_list:
            s += o
            s += '\n'
        ol.order = s
        ol.user = request.user
        ol.save()
        s = ''
        s = s + '/order/' +foo+'/check'
        return HttpResponseRedirect(s)


# def fw_submit(request):
#     if request.method == "POST":
#         ol = OrderList()
#         order_list = request.POST.getlist('options')
#         s = ''
#         option_list = Option.objects.filter(option=order_list[0])
#         ol.restaurant = option_list[0].restaurant
#         for o in order_list:
#             s += o
#             s += '\n'
#         ol.order = s
#         ol.user = request.user
#         ol.save()
#         return HttpResponseRedirect('/order/fw_check')
#
#
# def subway_submit(request):
#     if request.method == "POST":
#         ol = OrderList()
#         order_list = request.POST.getlist('options')
#         s = ''
#         option_list = Option.objects.filter(option=order_list[0])
#         ol.restaurant = option_list[0].restaurant
#         for o in order_list:
#             s += o
#             s += '\n'
#         ol.order = s
#         ol.user = request.user
#         p = 0
#         for o in order_list:
#             temp_list = Option.objects.filter(option=o)
#             p += temp_list[0].price
#
#         ol.price = p
#         ol.save()
#         return HttpResponseRedirect('/order/subway_check')
#
#
# def bnr_submit(request):
#     if request.method == "POST":
#         ol = OrderList()
#         order_list = request.POST.getlist('options')
#         s = ''
#         option_list = Option.objects.filter(option=order_list[0])
#         ol.restaurant = option_list[0].restaurant
#         for o in order_list:
#             s += o
#             s += '\n'
#         ol.order = s
#         ol.user = request.user
#         p = 0
#         for o in order_list:
#             temp_list = Option.objects.filter(option=o)
#             p += temp_list[0].price
#
#         ol.price = p
#         ol.save()
#         return HttpResponseRedirect('/order/bnr_check')


def check(request, foo):
    ol = OrderList.objects.filter(restaurant__name=foo)
    context = {'ol': ol}
    return render(request, 'order/check.html', context)


# def fw_check(request):
#     ol = OrderList.objects.filter(restaurant__name="Florentine")
#     context = {'ol': ol}
#     return render(request, 'order/check.html', context)
#
#
# def bnr_check(request):
#     ol = OrderList.objects.filter(restaurant__name="Baskin-Robbins")
#     context = {'ol': ol}
#     return render(request, 'order/check.html', context)
#
#
# def subway_check(request):
#     ol = OrderList.objects.filter(restaurant__name="Subway")
#     context = {'ol': ol}
#     return render(request, 'order/check.html', context)
