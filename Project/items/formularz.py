from django.forms import ModelForm
from .models import Item, Comment


class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'description', 'property', 'category', 'owner', 'shop', 'price']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment', 'update']
