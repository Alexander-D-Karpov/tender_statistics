# Generated by Django 4.1.7 on 2023-04-02 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0017_company_competetors"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="company",
            name="competetors",
        ),
        migrations.CreateModel(
            name="CompanyCompetetors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="competetors",
                        to="purchases.company",
                    ),
                ),
                (
                    "competetor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rev_competetors",
                        to="purchases.company",
                    ),
                ),
                (
                    "okved",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="purchases.okved",
                    ),
                ),
            ],
        ),
    ]
