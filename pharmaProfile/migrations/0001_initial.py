# Generated by Django 3.2.8 on 2021-10-29 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profileId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('nida', models.IntegerField(blank=True, null=True)),
                ('kura', models.IntegerField(blank=True, null=True)),
                ('licence', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('profileImage', models.ImageField(blank=True, editable=False, null=True, serialize=False, upload_to='')),
                ('is_boss', models.BooleanField(default=False, verbose_name='Boss')),
                ('can_add_medicine', models.BooleanField(default=False, verbose_name='Can Add Medicine?')),
                ('can_edit_medicine', models.BooleanField(default=False, verbose_name='Can Edit Medicine?')),
                ('can_delete_medicine', models.BooleanField(default=False, verbose_name='Can Delete Medicine?')),
                ('can_add_stock', models.BooleanField(default=False, verbose_name='Can Add Stock?')),
                ('can_edit_stock', models.BooleanField(default=False, verbose_name='Can Edit Stock?')),
                ('can_delete_stock', models.BooleanField(default=False, verbose_name='Can Delete Stock?')),
                ('can_add_sales', models.BooleanField(default=False, verbose_name='Can Make Sales?')),
                ('can_delete_sales', models.BooleanField(default=False, verbose_name='Can Remove Sales?')),
                ('can_add_salesman', models.BooleanField(default=False, verbose_name='Can Add Salesman?')),
                ('can_delete_salesman', models.BooleanField(default=False, verbose_name='Can Delete Salesman?')),
                ('can_generate_report', models.BooleanField(default=False, verbose_name='Can Print Report?')),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expensesId', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('expenseType', models.CharField(choices=[('', '--choose type--'), ('office', 'office'), ('personal', 'personal')], max_length=255)),
                ('expenseName', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]