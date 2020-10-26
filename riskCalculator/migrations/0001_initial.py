# Generated by Django 3.0.10 on 2020-10-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Que',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques1', models.CharField(max_length=120)),
                ('ques2', models.CharField(max_length=120)),
                ('ques3', models.CharField(max_length=120)),
                ('ques4', models.CharField(max_length=120)),
                ('ques5', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='RiskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(unique=True)),
                ('risk_score', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
