from django.shortcuts import render
from django.contrib.auth.models import User

def home(requests):
    return render(requests, "test.html")
