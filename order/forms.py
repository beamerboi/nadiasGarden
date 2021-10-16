from django import forms
from .models import Pizza, PizzaSize

# class PizzaForm(forms.Form):
# #   toppings = forms.MultipleChoiceField(choices=[('pep','pepperoni'),('cheese','Cheese'),('olives','Olives')], widget=forms.CheckboxSelectMultiple)
#     topping1 = forms.CharField(label = "Topping 1", max_length=100, required=True)
#     topping2 = forms.CharField(label = "Topping 2", max_length=100, required=True)
#     size = forms.ChoiceField(label="Size", choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], required=True)

class PizzaForm(forms.ModelForm):
    # size = forms.ModelChoiceField(queryset=PizzaSize.objects, empty_label=None, widget=forms.RadioSelect)
    # image = forms.ImageField()
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}

class MultiplePizazForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)