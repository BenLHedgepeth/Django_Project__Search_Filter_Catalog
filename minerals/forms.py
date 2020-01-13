from django.forms import Form, CharField, TextInput


class SearchForm(Form):
    query = CharField(
        max_length=255,
        widget=TextInput(attrs={
            'placeholder': "Search mineral info here..."
        })
    )
