from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse

import os

def home(request):
    return render(request, 'base/home.html')

