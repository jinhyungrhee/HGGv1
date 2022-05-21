# Generated by Django 4.0.4 on 2022-05-21 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0005_alter_apply_color_alter_apply_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='color',
            field=models.CharField(choices=[('red', 'Red'), ('beige', 'Beige'), ('purple', 'Purple')], max_length=20, null='True', verbose_name='색상'),
        ),
        migrations.AlterField(
            model_name='review',
            name='satisfaction',
            field=models.CharField(choices=[('3', '3'), ('5', '5'), ('2', '2'), ('4', '4'), ('1', '1')], max_length=10, verbose_name='만족도'),
        ),
    ]
