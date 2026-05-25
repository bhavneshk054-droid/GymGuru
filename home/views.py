from django.shortcuts import render
from datetime import date

from home.models import Contact


def home(request):
    return render(request, "index.html")


def index(request):
    context = {"variable1": "This is sent"}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc,
            date=date.today(),
        )

    return render(request, "contact.html")


