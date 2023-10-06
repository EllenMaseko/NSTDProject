from django.shortcuts import render

def sneaker_predict(request):
    context = {"x": 23}
    return render(request, "front.html", context)
