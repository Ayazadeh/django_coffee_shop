# Generated by Django 3.2.5 on 2021-07-22 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0004_auto_20210717_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitems',
            name='stimated_cooking_time',
        ),
        migrations.AddField(
            model_name='menuitems',
            name='estimated_cooking_time',
            field=models.TimeField(null=True, verbose_name='estimated cooking time:'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='deleted',
            field=models.BooleanField(verbose_name='delete'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='code',
            field=models.CharField(help_text='Enter Code for Discount', max_length=30, verbose_name='Enter Code:'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='deleted',
            field=models.BooleanField(verbose_name='delete'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='category',
            field=models.ForeignKey(help_text='Choose the group to which the item belongs', on_delete=django.db.models.deletion.CASCADE, to='menu_items.categories', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='deleted',
            field=models.BooleanField(verbose_name='delete'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='discount',
            field=models.ForeignKey(help_text='choice the discount', on_delete=django.db.models.deletion.CASCADE, to='menu_items.discount', verbose_name='discount:'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='price',
            field=models.ForeignKey(help_text='choice the price', on_delete=django.db.models.deletion.CASCADE, to='menu_items.price', verbose_name='price:'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='starting_cooking_time',
            field=models.TimeField(verbose_name='starting cooking time:'),
        ),
        migrations.AlterField(
            model_name='price',
            name='amount',
            field=models.IntegerField(help_text='The number you want to price', verbose_name='amount:'),
        ),
    ]