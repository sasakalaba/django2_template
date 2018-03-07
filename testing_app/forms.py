from django import forms


class CheckoutForm(forms.Form):
    COUNTRIES = (
        ('Austria', 'Austria'),
        ('Croatia', 'Croatia'),
        ('Italy', 'Italy')
    )
    BUDGET_RANGE = (
        ('< $100', '-100'),
        ('$100 - $499', '100/499'),
        ('$499 - $999', '499/999'),
        ('$999 >', '999')
    )
    ROOM_TYPE = (
        ('Single', 'Single'),
        ('Family', 'Family'),
        ('Business', 'Business')
    )

    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)
    country = forms.MultipleChoiceField(
        widget=forms.Select, choices=COUNTRIES, required=False)
    budget = forms.MultipleChoiceField(
        widget=forms.Select, choices=BUDGET_RANGE, required=False)
    room_type = forms.ChoiceField(choices=ROOM_TYPE, widget=forms.RadioSelect())
    room_description = forms.CharField(widget=forms.Textarea, max_length=500)
