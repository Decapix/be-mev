from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='Votre email', required=True)
    nom = forms.CharField(label='Votre nom', max_length=100, required=True)
    pour_email = forms.ChoiceField(label='Pour', choices=[('info@be-mev.com', 'info@be-mev.com'),
                                                          ('dtg@be-mev.com', 'dtg@be-mev.com'), 
                                                          ('amo@be-mev.com', 'amo@be-mev.com'), 
                                                          ('facture.mev@be-mev.com', 'facture.mev@be-mev.com'),
                                                          ('devis@be-mev.com', 'devis@be-mev.com'),
                                                          ('mar@be-mev.com', 'mar@be-mev.com')], required=True)
    message = forms.CharField(label='Votre message', widget=forms.Textarea, required=True)
