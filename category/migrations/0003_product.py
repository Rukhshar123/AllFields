# Generated by Django 3.1.4 on 2021-01-24 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now=True)),
                ('stock', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory')),
            ],
        ),
    ]
