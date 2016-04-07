# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputforms', '0006_auto_20160406_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitetype',
            name='site',
            field=models.CharField(choices=[(b'GRS', '\u0418\u0437\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0413\u0420\u0421'), (b'NPO', '\u0423\u0447\u0430\u0441\u0442\u043e\u043a NP, OP'), (b'BLK', '\u0411\u043b\u043e\u043a'), (b'CNT', '\u041a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440'), (b'SKD', '\u0421\u041a\u0418\u0414'), (b'KKP', '\u0421\u0431\u043e\u0440\u043a\u0430 \u0441\u0442\u0430\u043d\u0446\u0438\u0438'), (b'DUR', '\u0421\u0431\u043e\u0440\u043a\u0430 \u0434\u0432\u0435\u0440\u0438'), (b'VNT', '\u0412\u0435\u043d\u0442\u0438\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0440\u0435\u0448\u0451\u0442\u043a\u0430'), (b'EQI', '\u041c\u043e\u043d\u0442\u0430\u0436 \u041e\u0422 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f'), (b'ELI', '\u041c\u043e\u043d\u0442\u0430\u0436 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f'), (b'PIP', 'KVF-\u0442\u0440\u0443\u0431\u043e\u043f\u0440\u043e\u0432\u043e\u0434'), (b'GRB', '\u0413\u0420\u0411')], max_length=3),
        ),
        migrations.AlterField(
            model_name='workovertype',
            name='site',
            field=models.CharField(blank=True, choices=[(b'GRS', '\u0418\u0437\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0413\u0420\u0421'), (b'NPO', '\u0423\u0447\u0430\u0441\u0442\u043e\u043a NP, OP'), (b'BLK', '\u0411\u043b\u043e\u043a'), (b'CNT', '\u041a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440'), (b'SKD', '\u0421\u041a\u0418\u0414'), (b'KKP', '\u0421\u0431\u043e\u0440\u043a\u0430 \u0441\u0442\u0430\u043d\u0446\u0438\u0438'), (b'DUR', '\u0421\u0431\u043e\u0440\u043a\u0430 \u0434\u0432\u0435\u0440\u0438'), (b'VNT', '\u0412\u0435\u043d\u0442\u0438\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0440\u0435\u0448\u0451\u0442\u043a\u0430'), (b'EQI', '\u041c\u043e\u043d\u0442\u0430\u0436 \u041e\u0422 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f'), (b'ELI', '\u041c\u043e\u043d\u0442\u0430\u0436 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f'), (b'PIP', 'KVF-\u0442\u0440\u0443\u0431\u043e\u043f\u0440\u043e\u0432\u043e\u0434'), (b'GRB', '\u0413\u0420\u0411')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='worksonpathcard',
            name='time',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='site',
            field=models.CharField(blank=True, choices=[(b'GRS', '\u0418\u0437\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0413\u0420\u0421'), (b'NPO', '\u0423\u0447\u0430\u0441\u0442\u043e\u043a NP, OP'), (b'BLK', '\u0411\u043b\u043e\u043a'), (b'CNT', '\u041a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440'), (b'SKD', '\u0421\u041a\u0418\u0414'), (b'KKP', '\u0421\u0431\u043e\u0440\u043a\u0430 \u0441\u0442\u0430\u043d\u0446\u0438\u0438'), (b'DUR', '\u0421\u0431\u043e\u0440\u043a\u0430 \u0434\u0432\u0435\u0440\u0438'), (b'VNT', '\u0412\u0435\u043d\u0442\u0438\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0440\u0435\u0448\u0451\u0442\u043a\u0430'), (b'EQI', '\u041c\u043e\u043d\u0442\u0430\u0436 \u041e\u0422 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f'), (b'ELI', '\u041c\u043e\u043d\u0442\u0430\u0436 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f'), (b'PIP', 'KVF-\u0442\u0440\u0443\u0431\u043e\u043f\u0440\u043e\u0432\u043e\u0434'), (b'GRB', '\u0413\u0420\u0411')], max_length=3, null=True),
        ),
    ]