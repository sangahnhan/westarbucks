from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=45)
    class Meta:
        db_table="products_menu"
class Categories(models.Model):
    menu_id=models.ForeignKey('Menu',on_delete=models.CASCADE)
    name=models.CharField(max_length=45)

    class Meta:
        db_table="products_categories"

class Drinks(models.Model):
    categories_id=models.ForeignKey('Categories',on_delete=models.CASCADE)
    korean_name=models.CharField(max_length=45)
    english_name=models.CharField(max_length=45)
    description=models.TextField(max_length=200)
    allergies = models.ManyToManyField('Allergies','self')

    class Meta:
        db_table="products_drinks"

class Images(models.Model):
    image_url=models.CharField(max_length=2000)
    drinks_id=models.ForeignKey('Drinks',on_delete=models.CASCADE)
    class Meta:
        db_table="products_images"
        
class Allergies(models.Model):
    name=models.CharField(max_length=45)
    class Meta:
        db_table="products_allergy"

class Size(models.Model):
    name=models.CharField(max_length=45)
    size_ml=models.CharField(max_length=45)
    size_fluid_ounce=models.CharField(max_length=45)
    class Meta:
        db_table="products_size"

class Nutritions(models.Model):
    one_serving_kca=models.DecimalField(max_digits=10,decimal_places=2)
    sodium_mg=models.DecimalField(max_digits=10,decimal_places=2)
    fax_g=models.DecimalField(max_digits=10,decimal_places=2)
    sugars_g=models.DecimalField(max_digits=10,decimal_places=2)
    protein_g=models.DecimalField(max_digits=10,decimal_places=2)
    caffeine_mg=models.DecimalField(max_digits=10,decimal_places=2)
    drinks_id=models.ForeignKey('Drinks', on_delete=models.CASCADE)
    size_id=models.ForeignKey('Size', on_delete=models.CASCADE)
    class Meta:
        db_table="products_nutritions"