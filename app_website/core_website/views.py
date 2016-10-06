from core_main.utils import render


def home_view(request):
    return render(request, "core_website/home.html", {})


def help_view(request):
    return render(request, "core_website/help.html", {})
