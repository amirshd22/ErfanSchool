from django.shortcuts import render


def About(request):

    templates = 'About.html'
    context = {}
    return render(request, templates, context)