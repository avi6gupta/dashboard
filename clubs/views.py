from django.shortcuts import render
from .models import *


def club(request):
    c_list = Club.objects.all()
    context = {'c_list': c_list}
    return render(request, 'clubs/club.html', context)


def coding_club(request):
    # c_list = Club.objects.filter()
    p_list = Post.objects.filter(club__name="CodingClub")
    context = {'p_list': p_list}
    return render(request, 'clubs/post.html', context)


def robotics_club(request):
    # c_list = Club.objects.filter()
    p_list = Post.objects.filter(club__name="RoboticsClub")
    context = {'p_list': p_list}
    return render(request, 'clubs/post.html', context)


def montage(request):
    # c_list = Club.objects.filter()
    p_list = Post.objects.filter(club__name="Montage")
    context = {'p_list': p_list}
    return render(request, 'clubs/post.html', context)
