# Generated by Django 2.2 on 2019-04-25 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0007_auto_20190425_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(default='default', max_length=32)),
                ('prix', models.IntegerField(default=0)),
                ('type', models.CharField(default='default', max_length=32)),
                ('taille', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demandeDate', models.DateField(auto_now_add=True)),
                ('checkin', models.DateField(auto_now_add=True)),
                ('checkout', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='attendu', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Client')),
                ('demande', models.ManyToManyField(to='gestion.Ressource')),
            ],
        ),
    ]