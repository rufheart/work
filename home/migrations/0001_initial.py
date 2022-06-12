# Generated by Django 4.0.5 on 2022-06-12 18:17

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
            name='ABS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.abs')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='img/product')),
            ],
            bases=('home.abs',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.abs')),
                ('country', models.CharField(max_length=60)),
                ('price', models.CharField(max_length=50)),
                ('order_count', models.DecimalField(decimal_places=0, max_digits=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='home.product')),
            ],
            bases=('home.abs',),
        ),
    ]