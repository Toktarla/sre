# Generated by Django 2.2.19 on 2021-05-27 16:30
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0087_fix_attribute_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_identifier', models.CharField(help_text='Select the types of products this supplier can handle.Example for normal products select just Simple Supplier.', max_length=64, unique=True, verbose_name='module identifier')),
                ('name', models.CharField(help_text='Supplier modules name.', max_length=64, verbose_name='Module name')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='kind',
            field=models.IntegerField(choices=[(1, 'Product')], db_index=True, default=1),
        ),
        migrations.AddField(
            model_name='supplier',
            name='supplier_modules',
            field=models.ManyToManyField(blank=True, help_text='Select the supplier module to use for this supplier. Supplier modules define the rules by which inventory is managed.', related_name='suppliers', to='shuup.SupplierModule', verbose_name='supplier modules'),
        ),
    ]
