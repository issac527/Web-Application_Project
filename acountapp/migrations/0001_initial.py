# Generated by Django 3.2.4 on 2021-07-07 01:49

from django.db import migrations, models

# migration : # 변화를 반영하는 방법
# =============================================================
# makemigrations : Model 변경 사항 감지 및 변경 사항 반영할 파일 생성
# migrate
# =============================================================

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
