from django.shortcuts import render, HttpResponseRedirect
from .models import *


def signup_add(request):
    if request.method == 'POST':
        u = User()
        u.first_name = request.POST.get('first_name')
        u.last_name = request.POST.get('last_name')
        u.email = request.POST.get('email')
        u.username = request.POST.get('username')
        p = request.POST.get('password')
        q = request.POST.get('password2')
        if p == q:
            u.set_password(p)
            u.save()
            return HttpResponseRedirect('/order')
        else:
            return render(request, 'accounts/wrong_pswd.html')
    return render(request, 'accounts/dont_mess_with_us.html')


def signup(request):
    return render(request, "accounts/signup.html")


def secy_change(request):
    return render(request, 'accounts/secy_change.html')


def secy_changed(request):
    if request.method == 'POST' and request.user.is_authenticated :
        secy_list = Secy.objects.all()
        print("normal")
        for s in secy_list:
            if s.user == request.user:
                print("found secy")
                s1 = Secy()
                uname = request.POST.get('username')
                u = User.objects.filter(username=uname)
                s1.user = u[0]
                s1.club = s.club
                s1.save()
                s.delete()
                return render(request, 'accounts/successful.html')
    return render(request, 'accounts/dont_mess_with_us.html')


def manager_change(request):
    if request.method == 'POST':
        man_list = RestaurantManager.objects.all()
        for s in man_list:
            if s.user == request.user:
                uname = request.POST.get('username')
                u = User.objects.filter(username=uname)
                s.user = u
                s.save()
                return render(request, 'accounts/successful.html')
    return render(request, 'accounts/dont_mess_with_us.html')
