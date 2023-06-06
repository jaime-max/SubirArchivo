# Generated by Django 4.2.1 on 2023-06-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='pdfs/')),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
