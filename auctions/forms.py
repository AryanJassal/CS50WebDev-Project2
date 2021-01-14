from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Confirm Password"}))


class CreateListing(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "placeholder": "Description", "rows": "3"}))
    startingBid = forms.DecimalField(decimal_places=2, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "Starting Bid"}))
    imageURL = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': "form-control", "placeholder": "Image URL (optional)", "rows": "3"}))
