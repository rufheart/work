from django.shortcuts import render

def firstview(request):
    return render(request, 'ish.html')
