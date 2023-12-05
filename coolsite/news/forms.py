from .models import Artiles, Category, Author, Tag
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, SelectMultiple


from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Artiles, Category, Author, Tag

from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Artiles, Category, Author, Tag

class ArtilesForm(ModelForm):
    category_choice = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    category_new = forms.CharField(max_length=100, required=False)
    author_choice = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    author_new = forms.CharField(max_length=100, required=False)
    tag_choice = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False)
    tag_new = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва статі'
            }),

            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),

            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
        }

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        if self.cleaned_data['category_new']:
            category, created = Category.objects.get_or_create(name=self.cleaned_data['category_new'])
            instance.categories.add(category)
        else:
            instance.categories.add(self.cleaned_data['category_choice'])
        if self.cleaned_data['author_new']:
            author, created = Author.objects.get_or_create(name=self.cleaned_data['author_new'])
            instance.authors.add(author)
        else:
            instance.authors.add(self.cleaned_data['author_choice'])
        if self.cleaned_data['tag_new']:
            tag, created = Tag.objects.get_or_create(name=self.cleaned_data['tag_new'])
            instance.tags.add(tag)
        else:
            instance.tags.add(self.cleaned_data['tag_choice'])
        return instance


# class CategoryForm(ModelForm):
#   class Meta:
#     model = Category
#   fields = ['category']

# widgets = {
#   "category": TextInput(attrs={
#     'class': 'form-control',
#   'placeholder': 'Назва категорії'
# })
#  }
