
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


# Create your views here.
def home(request):
    current_user = "Jerry Plante"
    return render(request, "home.html",
                  {'login': current_user})


def motor_a(request):
    return render(request, "motor_a.html",
                  {"gradient1": "#3bf57fb5", "gradient2": "#3bf57f1c"})


def motor_b(request):
    return render(request, "motor_b.html",
                  {"gradient1": "#5798c9ad", "gradient2": "#3b41f521"})


def motor_c(request):
    return render(request, "motor_c.html",
                  {"gradient1": "#a73bf5ba", "gradient2": "#a43bf51a"})


def bumper_pull(request):
    return render(request, "bumper_pull.html",
                  {"gradient1": "#f5823bba", "gradient2": "#f57c3b1a"})


def fiver(request):
    return render(request, "fiver.html",
                  {"gradient1": "#afa337ba", "gradient2": "#f4cc031a"})


def training(request):
    return render(request, "training.html")


def about(request):
    return render(request, "about.html",
                  {"gradient1": "#e2f53b", "gradient2": "#e2f53b2b"})

def success(request):
    return render(request, "success.html",
                  {"gradient1": "#00000069", "gradient2": "#0000001a"})

def contact(request):
    if request.method == "POST":

        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # create an email
            name = form.cleaned_data['name']
            address = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            camper_type = form.cleaned_data['type']
            make = form.cleaned_data['make']
            seller = form.cleaned_data['seller']
            long = ("Name - "+name+"\n"+
                    "Email - "+address+"\n"+
                    "Phone - "+phone+"\n"+
                    "Type - "+camper_type+"\n"+
                    "Make - "+make+"\n"+
                    "Seller - "+seller+"\n"+
                    "Message\n"+message)
            send_mail('Web Contact from ' + name,
                       long,
                       address,
                      ['rvinspectionsne@gmail.com'],
                       fail_silently=False,
                      )
            return render(request, "success.html",
                {"gradient1": "#00000069", "gradient2": "#0000001a"})

    form = ContactForm()
    return render(request, "contact.html",
                      {"form": form,
                       "gradient1": "#00000069", "gradient2": "#0000001a"})
