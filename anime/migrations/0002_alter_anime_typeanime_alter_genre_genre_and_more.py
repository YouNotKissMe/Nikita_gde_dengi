# Generated by Django 4.0.4 on 2022-05-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='typeAnime',
            field=models.CharField(choices=[('film', 'фильм'), ('series', 'сериал'), ('spec', 'спешл'), ('clip', 'клип'), ('ova', 'ova'), ('ona', 'ona')], default='film', max_length=100, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(choices=[('senen', 'сёнен'), ('senen-ai', 'сёнен-ай'), ('seinen', 'сэйнен'), ('shojo', 'сёдзё'), ('shojo-ai', 'сёдзё-ай'), ('dzesei', 'дзёсей'), ('comedy', 'комедия'), ('romance', 'романтика'), ('school', 'школа'), ('madness', 'безумие'), ('martial_arts', 'боевые искусства'), ('vampires', 'вампиры'), ('war', 'военное'), ('harem', 'гарем'), ('gourmet', 'гурман'), ('demons', 'демоны'), ('detective', 'детектив'), ('baby', 'детское'), ('drama', 'драма'), ('historical', 'исторический'), ('space', 'космос'), ('games', 'игры'), ('magic', 'магия'), ('cars', 'машины'), ('furs', 'меха'), ('music', 'музыка'), ('parody', 'пародия'), ('everyday life', 'повседневность'), ('police', 'полиция'), ('adventure', 'приключение'), ('psychological', 'психологическое'), ('work', 'работа'), ('samurai', 'самураи'), ('supernatural', 'сверхъестественное'), ('sport', 'спорт'), ('super power', 'супер сила'), ('horrors', 'ужасы'), ('fantastic', 'фантастика'), ('fantasy', 'фэнтези'), ('action', 'экшен'), ('etty', 'этти'), ('thriller', 'триллер')], default=('senen', 'сёнен'), max_length=13, primary_key=True, serialize=False, unique=True, verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='AnimeType',
        ),
    ]
