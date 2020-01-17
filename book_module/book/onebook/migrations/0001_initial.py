# Generated by Django 2.2.9 on 2020-01-17 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oneauthor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('publication_date', models.DateTimeField(null=True, verbose_name='Book publication datetime')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneauthor.Author')),
            ],
        ),
    ]