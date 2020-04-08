# Generated by Django 2.2.10 on 2020-04-07 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0003_auto_20200402_1151'),
        ('lawmaker', '0010_auto_20200406_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activelawmaker',
            name='attend_rate',
            field=models.CharField(blank=True, max_length=8, verbose_name='출석률'),
        ),
        migrations.CreateModel(
            name='Candidacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('name_en', models.CharField(blank=True, max_length=20, verbose_name='영어 이름')),
                ('name_cn', models.CharField(blank=True, max_length=20, verbose_name='한자 이름')),
                ('gender', models.CharField(choices=[('m', '남성'), ('f', '여성'), ('n', '중성'), ('x', '표기안함')], max_length=10)),
                ('party', models.CharField(blank=True, max_length=10, verbose_name='정당')),
                ('birthday', models.CharField(blank=True, max_length=30)),
                ('education', models.TextField(blank=True, verbose_name='학력정보')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='주소')),
                ('career', models.CharField(blank=True, max_length=255, verbose_name='커리어')),
                ('image', models.FileField(blank=True, null=True, upload_to='person/', verbose_name='이미지 파일')),
                ('image_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='이미지 url')),
                ('job', models.CharField(blank=True, max_length=30, verbose_name='직업')),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('blog', models.CharField(blank=True, max_length=255)),
                ('page', models.CharField(blank=True, max_length=255)),
                ('wiki', models.TextField(blank=True, verbose_name='추가 정보')),
                ('extra_info', models.TextField(blank=True, verbose_name='추가 정보')),
                ('nec_id', models.CharField(blank=True, max_length=20)),
                ('num', models.CharField(blank=True, max_length=30, verbose_name='기호')),
                ('property', models.CharField(blank=True, max_length=12, verbose_name='재산')),
                ('military_info', models.CharField(blank=True, max_length=10, verbose_name='병역')),
                ('payed_tax', models.CharField(blank=True, max_length=12, verbose_name='재산')),
                ('not_pay_tax_five', models.CharField(blank=True, max_length=12, verbose_name='최근 5년간 체납금액')),
                ('not_pay_tax_current', models.CharField(blank=True, max_length=12, verbose_name='현재채납급액')),
                ('conviction_count', models.CharField(blank=True, max_length=10, verbose_name='전과')),
                ('candidacy_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='입후보')),
                ('type', models.CharField(choices=[('R', '비례'), ('D', '지역구')], max_length=10)),
                ('assembly_id', models.CharField(choices=[('21', '21대')], max_length=10)),
                ('district', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='district.District', verbose_name='지역구')),
            ],
        ),
    ]
