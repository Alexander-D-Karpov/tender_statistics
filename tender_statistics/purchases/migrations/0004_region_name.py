# Generated by Django 4.1.7 on 2023-04-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0003_alter_kpgz_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="region",
            name="name",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
