from django.views import generic

class CalculatorView(generic.TemplateView):
    template_name="calculator.html"

#CRUD Views
#Create, Read, Update, Delete

from Calculator.models import calculator_history
class CalculatorCreateView(generic.CreateView):
    template_name="calculator/create.html"
    queryset=calculator_history.objects.all()
    fields="__all__"

class CalculatorReadView(generic.ListView):
    template_name="calculator/index.html"
    queryset=calculator_history.objects.all()
    context_object_name="objects"
    # by default

class CalculatorUpdateView(generic.UpdateView):
    template_name="calculator/update.html"
    queryset=calculator_history.objects.all()
    fields="__all__"

class CalculatorDeleteView(generic.DeleteView):
    template_name="calculator/delete.html"
    queryset=calculator_history.objects.all()