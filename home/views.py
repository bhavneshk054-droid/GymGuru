from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def home(request):
    return render(request, "index.html")
def index(request):
    context = { "variable1": "This is sent" }
    return render(request, "index.html", context)
def about(request):
  #  return HttpResponse("This is the about page.")
    return render(request, "about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        data = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        data.save()
    # return HttpResponse("This is the contact page.")
    return render(request, "contact.html")

