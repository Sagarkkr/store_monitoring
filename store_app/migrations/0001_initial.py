# Generated by Django 4.2.4 on 2023-08-08 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('store_id', models.CharField(max_length=100, unique=True)),
                ('timezone_str', models.CharField(default='America/Chicago', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uptime_last_hour', models.BigIntegerField()),
                ('uptime_last_day', models.BigIntegerField()),
                ('uptime_last_week', models.BigIntegerField()),
                ('downtime_last_hour', models.BigIntegerField()),
                ('downtime_last_day', models.BigIntegerField()),
                ('downtime_last_week', models.BigIntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_reports', to='store_app.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('timestamp_utc', models.DateTimeField(db_index=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], max_length=10)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_status_updates', to='store_app.store')),
            ],
            options={
                'verbose_name': 'Store Status',
                'unique_together': {('store', 'timestamp_utc')},
            },
        ),
        migrations.CreateModel(
            name='BusinessHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('day_of_week', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (0, 'Sunday')])),
                ('start_time_local', models.TimeField()),
                ('end_time_local', models.TimeField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_business_hours', to='store_app.store')),
            ],
            options={
                'verbose_name': 'Business Hour',
                'unique_together': {('store', 'day_of_week')},
            },
        ),
    ]