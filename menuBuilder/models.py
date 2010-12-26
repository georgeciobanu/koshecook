from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=90, primary_key=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Store(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=900)
    
    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=300, primary_key=True)
    stores = models.ManyToManyField(Store)

    def __unicode__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=90, primary_key=True)
    baseMultiplier = models.DecimalField(max_digits=10,decimal_places=3)
    base = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.name


class IngredientInstance(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.ForeignKey(Unit) 

    def __unicode__(self):
        return str(self.quantity) + ' ' + str(self.unit) + ' ' + self.ingredient.name

class Recipe(models.Model):
    name = models.CharField(max_length=300)
    ingredients = models.ManyToManyField(IngredientInstance)
    instructions = models.TextField()
    servings = models.DecimalField(max_digits=5, decimal_places=1)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name

class CategoryInstance(models.Model):
    category = models.ForeignKey(Category) 
    serving_order = models.SmallIntegerField()   
    
    def __unicode__(self):
        return self.category.name + ' ' + str(self.serving_order) 

class MenuTemplate(models.Model):
    name = models.CharField(max_length=90)
    items = models.ManyToManyField(CategoryInstance)
    
    def __unicode__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=90)
    template = models.ForeignKey(MenuTemplate)
    items = models.ManyToManyField(Recipe)

    def __unicode__(self):
        return self.name

