# Generated by Django 4.0.2 on 2022-11-21 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('college', models.CharField(choices=[('HU', '인문과학계열(HUMANITY)'), ('SO', '사회과학계열(SOCIETY)'), ('SC', '자연과학계열(SCIENCE)'), ('EN', '공학계열(ENGINNERING)')], default='HU', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(db_column='post_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='snsapp.post')),
            ],
        ),
    ]
