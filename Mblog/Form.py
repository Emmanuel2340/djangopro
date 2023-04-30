from django import forms
from blog.models import Post,Category


lists = []
choices = Category.objects.all().values_list("name", "name")
for item in choices:
    lists.append(item)

class FormClass(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('author','title','category', 'body','price')

        widgets={
            "title" :forms.TextInput(attrs={'class': 'form-control',"placeholder":lists}),
            'author':forms.Select(attrs={"class": "form-control"}),
            'category':forms.Select(choices=lists, attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }

        
class EditForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('author','title','category', 'body')

        widgets={
            "title" :forms.TextInput(attrs={'class': 'form-control',"placeholder":"me"}),
            'author':forms.Select(attrs={"class": "form-control"}),
            'category':forms.Select(choices=choices, attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

        