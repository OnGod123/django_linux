from django.shortcuts import render

def my_view(request):
    # Your view logic here
    return render(request, 'myapp/my_template.html', context)

