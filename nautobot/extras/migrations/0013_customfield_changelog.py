# Generated by Django 3.1.13 on 2021-08-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0012_relationshipassociation_changelog"),
    ]

    operations = [
        migrations.AddField(
            model_name="customfield",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="customfield",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
