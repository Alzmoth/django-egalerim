# Generated by Django 2.2.3 on 2019-12-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cariekle', '0002_auto_20191201_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cariekle',
            name='vergi_dairesi',
        ),
        migrations.AddField(
            model_name='cariekle',
            name='posta_kodu',
            field=models.IntegerField(default=42020),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cariekle',
            name='tc_no',
            field=models.IntegerField(default=33655965912),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cariekle',
            name='vergi_no',
            field=models.IntegerField(blank=True),
        ),
    ]