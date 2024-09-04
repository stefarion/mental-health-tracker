from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152456',
        'name': 'Stefanus Tan Jaya',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)