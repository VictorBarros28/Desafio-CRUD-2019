# Generated by Django 2.2.4 on 2019-08-09 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_auto_20190808_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsFromPost', to='posts.Post', verbose_name='Post:'),
        ),
    ]
