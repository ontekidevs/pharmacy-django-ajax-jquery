from django.db import models
from django.utils.translation import gettext_lazy as _
from configurations import utils


class Medicine(models.Model):
    medicineId = models.AutoField(primary_key= True)
    medicineName = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    genericName = models.CharField(max_length=255)
    form = models.ForeignKey('MedicineForm', on_delete=models.CASCADE, null=True, blank=True)
    discount = models.IntegerField(default=0)
    sideEffect = models.CharField(max_length=255,null=True, blank=True)
    slug = models.SlugField(_("identifier"), null=True, blank=True, unique=True)
    image = models.ImageField(null = True, blank = True)
    addedDate = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return str(self.medicineName)

class MedicineForm(models.Model):
    medicineFormId = models.AutoField(primary_key= True)
    medicineFormName = models.CharField(max_length=255)

    def __str__(self):
        return self.medicineFormName


class Category(models.Model):
    categoryId = models.AutoField(primary_key= True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(_("identifier"), null=True, blank=True, unique=True)


    def save(self):
        self.slug = utils.slugify(self.title)
        return super().save()

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name_plural = 'Categories'
