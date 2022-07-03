from django.shortcuts import render, get_object_or_404
from .models import Item, Update, Champion, Comment, Shop
from .formularz import ItemForm, CommentForm
from django.shortcuts import redirect

def item_list(request):
    wszystkie = Item.objects.all()
    ilosc = len(wszystkie)
    return render(request, 'items/item_list.html', {'items': wszystkie,
    'ile': ilosc })

def form_f(request):
    formularz = ItemForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(item_list)
    return render(request, 'formularz.html', {'form': formularz})

def edycja_f(request, id):
    item = get_object_or_404(Item, pk=id)
    formularz = ItemForm(request.POST or None, request.FILES or None, instance=item)
    if formularz.is_valid():
        formularz.save()
        return redirect(item_list)
    return render(request, 'edycja.html', {'form': formularz})

def usun_f(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        item.delete()
        return redirect(item_list)
    return render(request, 'usun.html', {'id_item': item})

def update_(request):
    update = Update.objects.all()
    komentarz = Comment.objects.all()
    return render(request, 'update.html', {'updates': update, 'comments': komentarz})

def comment_(request):
    komentarz = CommentForm(request.POST or None, request.FILES or None)
    if komentarz.is_valid():
        komentarz.save()
        return redirect(update_)
    return render(request, 'komentarz.html', {'comments': komentarz})

def champion_(request):
    champion = Champion.objects.all()
    shop = Shop.objects.all()
    ilosc = len(champion)
    return render(request, 'champion.html', {'champs': champion, 'shops': shop,
    'ile': ilosc })

def item_(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'items/item.html', {'item': item})



