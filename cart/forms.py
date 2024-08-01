from django import forms

PRODUCT_QUANTITY = [(i, str(i)) for i in range(1,21)]

class AddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY, coerce=int,label='Количество')
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)