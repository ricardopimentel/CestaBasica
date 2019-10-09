from django.forms import ModelForm
from .models import pesquisa_preco

# Create the form class.
class PrecoForm(ModelForm):
    class Meta:
        model = pesquisa_preco
        fields = ['preco', 'estabelecimento', 'produto']

class PrecoFormCad(ModelForm):
    class Meta:
        model = pesquisa_preco
        fields = ['preco', 'estabelecimento', 'produto', 'evento']