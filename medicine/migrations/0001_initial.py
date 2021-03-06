# Generated by Django 3.2.8 on 2021-10-29 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='identifier')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MedicineForm',
            fields=[
                ('medicineFormId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineFormName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicineId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineName', models.CharField(max_length=255)),
                ('genericName', models.CharField(max_length=255)),
                ('discount', models.IntegerField(default=0)),
                ('sideEffect', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='identifier')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('addedDate', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.category')),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.medicineform')),
            ],
        ),
    ]
