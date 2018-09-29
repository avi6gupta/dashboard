from django.shortcuts import render, HttpResponseRedirect
from .models import *
from accounts.models import Secy

def club(request):
    c_list = Club.objects.all()
    context = {'c_list': c_list}
    return render(request, 'clubs/club.html', context)


def club_type(request, foo):
    p_list = Post.objects.filter(club__name=foo)
    context = {'p_list': p_list}
    return render(request, 'clubs/post.html', context)


def add(request, foo):
    if request.user.is_authenticated:
        secy_list = Secy.objects.filter(club=foo)
        context = {'secy_list': secy_list}
        p = Post()
        for s in secy_list:
            if s.user == request.user:
                if request.method == 'POST':
                    image = request.FILES.get('file')
                    p.img = image
                    p.post = request.POST.get('txt')
                    p.club = Club.objects.filter(name=foo)[0]
                    p.save()
                return render(request, 'clubs/add.html', context)
        return render(request, 'clubs/not_secy.html')
    return HttpResponseRedirect('/login')
