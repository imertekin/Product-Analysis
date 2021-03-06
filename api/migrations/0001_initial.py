# Generated by Django 3.2.7 on 2021-09-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('index', models.AutoField(auto_created = True,primary_key=True, serialize=False)),
                ('P_id', models.BigIntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('images', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('ratingscore', models.FloatField(blank=True, db_column='ratingScore', null=True)),
                ('totalcount', models.FloatField(blank=True, db_column='totalCount', null=True)),
                ('categoryhierarchy', models.TextField(blank=True, db_column='categoryHierarchy', null=True)),
                ('categoryid', models.BigIntegerField(blank=True, db_column='categoryId', null=True)),
                ('categoryname', models.TextField(blank=True, db_column='categoryName', null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('sellingppice', models.FloatField(blank=True, db_column='sellingpPice', null=True)),
                ('originalprice', models.FloatField(blank=True, db_column='originalPrice', null=True)),
                ('discountedprice', models.FloatField(blank=True, db_column='discountedPrice', null=True)),
                ('freecargo', models.BooleanField(blank=True, db_column='freeCargo', null=True)),
                ('addedtime', models.DateTimeField(blank=True, db_column='addedTime', null=True)),
            ],
            options={
                'db_table': 'JsonProduct',
                'managed': False,
            },
        ),
    ]
