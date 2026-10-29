from django import forms

class ContactForm(forms.Form):

    TYPE_CHOICES = (
        ('class_a', 'Class A',),
        ('class_b', 'Class B/B+',),
        ('class_c', 'Class C',),
        ('travel_trailer', 'Travel Trailer',),
        ('fifth_wheel', 'Fifth Wheel',),
    )
    SELLER_CHOICES = (
      ('private', "Private Seller",),
      ('dealer', "Dealer",),
    )

    name = forms.CharField(label='Name', max_length=50,
                widget=forms.Textarea(
                    attrs={ 'class':'contact-textarea', 'cols': 20, 'rows':1}))
    phone = forms.CharField(label='Phone', max_length=12, required=False,
                widget=forms.Textarea(
                    attrs={ 'class':'contact-textarea', 'cols': 20, 'rows':1}))
    email = forms.EmailField(label='Email', max_length=50,
                widget = forms.Textarea(
                    attrs={'class': 'contact-textarea', 'cols': 20, 'rows': 1}))
    type = forms.ChoiceField(label='Type', choices=TYPE_CHOICES)
    make = forms.CharField(label='Make and Model', max_length=70,
                widget=forms.Textarea(
                    attrs={'class': 'contact-textarea', 'cols': 20, 'rows': 1}))
    seller= forms.ChoiceField(label='Seller', choices=SELLER_CHOICES,
            widget=forms.RadioSelect(attrs={ 'class': 'form-check form-check-inline contact-radio', }))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'contact-textarea','rows': 5, 'cols': 40, }),
            max_length=500,
            initial="Location:\nMessage:")

# Yeah, I tried crispy - not enough control over where the fields go on the form
class ContactFormMobile(forms.Form):

    TYPE_CHOICES = (
        ('class_a', 'Class A',),
        ('class_b', 'Class B/B+',),
        ('class_c', 'Class C',),
        ('travel_trailer', 'Travel Trailer',),
        ('fifth_wheel', 'Fifth Wheel',),
    )
    SELLER_CHOICES = (
      ('private', "Private Seller",),
      ('dealer', "Dealer",),
    )

    name = forms.CharField(label='Name', max_length=50,
                widget=forms.Textarea(
                    attrs={ 'class':'contact-textarea', 'cols': 20, 'rows':1}))
    phone = forms.CharField(label='Phone', max_length=12, required=False,
                widget=forms.Textarea(
                    attrs={ 'class':'contact-textarea', 'cols': 20, 'rows':1}))
    email = forms.EmailField(label='Email', max_length=50,
                widget = forms.Textarea(
                    attrs={'class': 'contact-textarea', 'cols': 20, 'rows': 1}))
    type = forms.ChoiceField(label='Type', choices=TYPE_CHOICES)
    make = forms.CharField(label='Make and Model', max_length=70,
                widget=forms.Textarea(
                    attrs={'class': 'contact-textarea', 'cols': 20, 'rows': 1}))
    seller= forms.ChoiceField(label='Seller', choices=SELLER_CHOICES,
            widget=forms.RadioSelect(attrs={ 'class': 'form-check form-check-inline contact-radio', }))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'contact-textarea','rows': 5, 'cols': 30, }),
            max_length=500,
            initial="Location:\nMessage:")