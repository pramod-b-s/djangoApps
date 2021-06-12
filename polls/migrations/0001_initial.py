# Generated by Django 3.2.4 on 2021-06-12 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default='Question text', max_length=50)),
                ('pub_date', models.DateTimeField(auto_now=True, null=True)),
                ('choice_one', models.CharField(default='choice one', max_length=50)),
                ('choice_two', models.CharField(default='choice two', max_length=50)),
                ('choice_three', models.CharField(default='choice three', max_length=50)),
                ('votes_one', models.IntegerField(default=0)),
                ('votes_two', models.IntegerField(default=0)),
                ('votes_three', models.IntegerField(default=0)),
                ('pollcreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
