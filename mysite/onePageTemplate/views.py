from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, "onePageTemplate_base.html")


def janFitzner(request):
    context = {
        "NAV_TITEL": "Architektur",
        "NAV_SUBTITEL": "Jan Fitzner",
        "CONTACT_ADRESS": "Schulberg 3, 99955, Bad Tennstedt",
        "CONTACT_PHONE": "+49 36041 33352",
        "CONTACT_MOBIL": "+49 1624 342104",
        "CONTACT_EMAIL": "info@janfitzner.de",
    }

    return render(request, "janFitzner.html", context)


def tinker(request):
    return render(request, "tinker.html")


def legalnotice(request):
    context = {
        "NAV_TITEL": "Architektur",
        "NAV_SUBTITEL": "Jan Fitzner",
        "CONTACT_ADRESS": "Schulberg 3, 99955, Bad Tennstedt",
        "CONTACT_PHONE": "+49 36041 33352",
        "CONTACT_MOBIL": "+49 1624 342104",
        "CONTACT_EMAIL": "info@janfitzner.de",
    }
    return render(request, "onePageTemplate_legalnotice.html", context)
