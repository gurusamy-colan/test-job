# Generated by Django 4.2.7 on 2023-11-20 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BusinessInvestor',
            new_name='BusinessInvestorType',
        ),
        migrations.AlterModelTable(
            name='businessinvestortype',
            table='business_investor_type',
        ),
    ]