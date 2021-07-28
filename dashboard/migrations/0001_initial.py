# Generated by Django 3.2.5 on 2021-07-27 13:58

import datetime
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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=50)),
                ('Created_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=100, null=True)),
                ('Product_Quantity', models.PositiveIntegerField(null=True)),
                ('Created_Date', models.DateTimeField(auto_now=True)),
                ('Created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Product_Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Quantity', models.PositiveIntegerField(null=True)),
                ('Issued_Quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('Phone', models.CharField(max_length=100, null=True)),
                ('Email', models.CharField(max_length=100, null=True)),
                ('Created_Date', models.DateTimeField(auto_now=True)),
                ('Updated_Date', models.DateTimeField(auto_now=True)),
                ('Order_Name_Of_Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
