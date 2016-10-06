from django.shortcuts import render


def template_test(request):
    return render(request, "base.html")
