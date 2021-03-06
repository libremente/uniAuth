# Generated by Django 2.2.4 on 2019-08-15 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unical_accounts', '0003_auto_20190730_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='persistent_id',
        ),
        migrations.CreateModel(
            name='PersistentId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persistent_id', models.CharField(blank=True, max_length=254, null=True, verbose_name='SAML Persistent Stored ID')),
                ('recipient_id', models.CharField(blank=True, max_length=254, null=True, verbose_name='SAML ServiceProvider entityID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
