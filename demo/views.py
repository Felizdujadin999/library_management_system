from django.http import HttpResponse


def welcome(request):
    return HttpResponse("welcome Mr sikiru, what can i help you with today?...")
