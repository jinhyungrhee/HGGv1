# Generated by Django 4.0.4 on 2022-05-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0003_alter_apply_color_alter_review_satisfaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('L', 'Large'), ('M', 'Medium')], max_length=10, null='True', verbose_name='사이즈'),
        ),
        migrations.AlterField(
            model_name='review',
            name='satisfaction',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('4', '4'), ('5', '5'), ('3', '3')], max_length=10, verbose_name='만족도'),
        ),
    ]
