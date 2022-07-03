from django.db import models
from django.utils import timezone


class Property(models.Model):
    RARITIES = [
        ('CO', 'Common'),
        ('UN', 'Uncommon'),
        ('RA', 'Rare'),
        ('EP', 'Epic'),
        ('LE', 'Legendary'),
    ]
    WEARS = [
        ('NE', 'New'),
        ('SW', 'Slightly Worn'),
        ('HW', 'Heavily Worn'),
        ('DE', 'Destroyed'),
    ]
    rarity = models.CharField(max_length=50, choices=RARITIES)
    wear = models.CharField(max_length=50, choices=WEARS)
    damage = models.PositiveIntegerField()
    damage_blocked = models.PositiveIntegerField()

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.rarity, self.wear, self.damage, self.damage_blocked)


class Category(models.Model):
    CATEGORIES = [
        ('OF', 'Offensive'),
        ('DE', 'Defensive'),
        ('HE', 'Healing'),
        ('MA', 'Magic')
    ]
    RANGE = [
        ('LO', 'Low Range'),
        ('ME', 'Medium Range'),
        ('LN', 'Long Range')
    ]
    ORIGINS = [
        ('CD', 'Chest Drop'),
        ('BD', 'Boss Drop'),
        ('SH', 'Shop'),
        ('CR', 'Crafting')
    ]
    CRAFTABLE = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    category = models.CharField(max_length=50, choices=CATEGORIES)
    range = models.CharField(max_length=50, choices=RANGE)
    origin = models.CharField(max_length=50, choices=ORIGINS)
    craftable = models.CharField(max_length=50, choices=CRAFTABLE)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.category, self.range, self.origin, self.craftable)


class Champion(models.Model):
    CLASSES = [
        ('MA', 'Mage'),
        ('WA', 'Warrior'),
        ('HE', 'Healer'),
        ('TA', 'Tank')
    ]
    RACES = [
        ('OR', 'Orc'),
        ('HU', 'Human'),
        ('EL', 'Elf')
    ]
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField()
    champ_class = models.CharField(max_length=50, choices=CLASSES)
    guild = models.CharField(max_length=50, choices=RACES)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50)
    owner = models.OneToOneField(Champion, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    money = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(Champion, on_delete=models.CASCADE, blank=True, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    description = models.TextField()

    def __str__(self):
        return self.name


class Update(models.Model):
    name = models.CharField(max_length=50)
    version = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ability(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    cooldown = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    update = models.ForeignKey(Update, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name