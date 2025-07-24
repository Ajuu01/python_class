from django.shortcuts import render

def calculator_view (request):
    if request.method=="POST":
        form_data=request.POST
        print(form_data)
    context={

    }
    return render(request,"calculator.html",context)