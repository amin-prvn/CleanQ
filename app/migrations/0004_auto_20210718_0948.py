# Generated by Django 3.2.3 on 2021-07-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210718_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='backup',
            name='action',
        ),
        migrations.AlterField(
            model_name='backup',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='backup'),
        ),
    ]
