from django import forms
from diogenes.models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Title:")
    author = forms.CharField(widget=forms.HiddenInput(), required=False)
    first_name = forms.CharField(max_length=128, help_text="Author first name:")
    last_name = forms.CharField(max_length=128, help_text="Author last name:")
    year = forms.IntegerField(required=False, help_text="Year published:")
    publisher = forms.CharField(max_length=128, help_text="Publisher:")
    ISBN = forms.CharField(max_length=128, required=False, help_text="ISBN:")
    genre = forms.CharField(max_length=128, required=False, help_text="Genre:")
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Book
        exclude = ('author', 'user')

    """def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BookForm, self).__init__(*args, **kwargs)"""