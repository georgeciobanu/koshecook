
from django.contrib import admin
from KosheCook.menuBuilder.models import Category, Store, Ingredient, Recipe, MenuTemplate, Menu, IngredientInstance, CategoryInstance, Unit

#class CategoryAdmin(admin.ModelAdmin):
#    verbose_name_plural = "Categories"

admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Ingredient)
admin.site.register(IngredientInstance)
admin.site.register(CategoryInstance)
admin.site.register(Recipe)
admin.site.register(MenuTemplate)
admin.site.register(Menu)
admin.site.register(Unit)
