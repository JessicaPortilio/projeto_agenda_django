from contact.models import Contact
from django import forms 
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                        'class':'classe-a classe-b',
                        'placeholder' : 'Escreva aquiiiiiiiii',
                    }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário'
    )
    qualquer = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                        'class':'classe-a classe-b',
                        'placeholder' : 'Escreva aquiiiiiiiii',
                    }
        ),
        help_text='Texto de ajuda para seu usuário'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields ['first_name'].widget.attrs.update({
        #     'class':'classe-a classe-b',
        #     'placeholder' : 'Escreva aqui veio do init'
        # })
        
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone'
            )
        
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs= {
        #             'class':'classe-a classe-b',
        #             'placeholder' : 'Escreva aqui'
        #         }
        #     )
        # }
    
    def clean(self):
        # cleaned_data = self.cleaned_data
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        
        return super().clean()