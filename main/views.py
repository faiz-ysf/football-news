from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406434292',
        'name': 'Faiz Yusuf Ridwan',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
