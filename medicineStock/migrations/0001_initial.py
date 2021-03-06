# Generated by Django 3.2.8 on 2021-10-29 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicine', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purcahaseId', models.AutoField(primary_key=True, serialize=False)),
                ('stockName', models.CharField(blank=True, max_length=255, null=True)),
                ('dueDate', models.DateField(auto_now_add=True, null=True)),
                ('sellingPrice', models.IntegerField(blank=True, null=True)),
                ('buyingPrice', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('expireDate', models.DateField(blank=True, null=True)),
                ('addedBy', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stockId', models.AutoField(primary_key=True, serialize=False)),
                ('stockName', models.CharField(blank=True, max_length=255, null=True)),
                ('expireDate', models.DateField(blank=True, null=True)),
                ('tako', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('buyingPrice', models.IntegerField(blank=True, null=True)),
                ('_profit', models.IntegerField(blank=True, null=True)),
                ('sellingPrice', models.IntegerField(blank=True, null=True)),
                ('addedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('medicineId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
            ],
        ),
    ]
