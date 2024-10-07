# Generated by Django 5.1.1 on 2024-10-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0003_person_delete_employee_delete_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_location', models.CharField(max_length=40)),
                ('room_capacity', models.IntegerField(max_length=10)),
                ('room_review', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_name', models.CharField(max_length=50)),
                ('collge_location', models.CharField(max_length=70)),
                ('college_distance', models.FloatField(max_length=10)),
                ('college_review', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='classroom',
            name='room_name',
            field=models.ManyToManyField(to='myfirstapp.college'),
        ),
    ]
