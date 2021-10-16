from django.shortcuts import render
from .forms import PizzaForm, MultiplePizazForm
from django.forms import formset_factory
from .models import Pizza
# Create your views here.

def home(request):
    return render(request, 'order/home.html')

def order(request):
    multiple_form = MultiplePizazForm()
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = f"Thanks for ordering! Your {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} and {filled_form.cleaned_data['topping2']} Pizza is on its way"  
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = "Pizza order has faild, please try again!"
        return render(request, 'order/order.html', {'created_pizza_pk':created_pizza_pk,'pizza': filled_form, 'note':note, "multiple_form":multiple_form})
    else: 
        pizza = PizzaForm()
        return render(request, 'order/order.html', {'pizza': pizza, "multiple_form":multiple_form})

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizazForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas Have Been Ordered!'
        else:
            note = "Order was not created, please try again!"
        
        return render(request, 'order/pizza.html', {'note': note, 'formset':formset})
    else:
        return render(request, 'order/pizza.html', {'formset':formset})

def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note="Changes has been updated"
            return render(request, 'order/edit_order.html', {'note':note, 'pizzaform':form, 'pizza':pizza})

    return render(request, 'order/edit_order.html', {'pizzaform':form, 'pizza':pizza})
