# Generated by Django 3.0.6 on 2020-06-15 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttc_rest_api', '0002_ttc_comment_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttc_comment_tb',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ttc_rest_api.TTC_POST_TB'),
        ),
    ]
