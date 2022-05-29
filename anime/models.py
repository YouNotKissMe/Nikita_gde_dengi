from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
def MAX(choices):
    max = None
    for i in choices:
        if max:
            if max < len(i[0]):
                max = len(i[0])
        else:
            max = len(i[0])
    return max


choices = [('announced', 'анонсированно'),
           ('coming', 'выходит'),
           ('ready', 'вышло'),
           ('pause', 'приостановленно'),
           ('error', 'отменено')]
choices_max_length = MAX(choices)
choices_rating = [(None, 'Пока не оценено'),
                  (1, 'Мои Глаза'),
                  (2, 'Жалко потраченного времени'),
                  (3, 'Проект на один раз'),
                  (4, 'Хороий проект'),
                  (5, 'Проект нашел отклик в моей душе')]


class Genre(models.Model):
    choices = [
        ('senen', 'сёнен'),
        ('senen-ai', 'сёнен-ай'),
        ('seinen', 'сэйнен'),
        ('shojo', 'сёдзё'),
        ('shojo-ai', 'сёдзё-ай'),
        ('dzesei', 'дзёсей'),
        ('comedy', 'комедия'),
        ('romance', 'романтика'),
        ('school', 'школа'),
        ('madness', 'безумие'),
        ('martial_arts', 'боевые искусства'),
        ('vampires', 'вампиры'),
        ('war', 'военное'),
        ('harem', 'гарем'),
        ('gourmet', 'гурман'),
        ('demons', 'демоны'),
        ('detective', 'детектив'),
        ('baby', 'детское'),
        ('drama', 'драма'),
        ('historical', 'исторический'),
        ('space', 'космос'),
        ('games', 'игры'),
        ('magic', 'магия'),
        ('cars', 'машины'),
        ('furs', 'меха'),
        ('music', 'музыка'),
        ('parody', 'пародия'),
        ('everyday life', 'повседневность'),
        ('police', 'полиция'),
        ('adventure', 'приключение'),
        ('psychological', 'психологическое'),
        ('work', 'работа'),
        ('samurai', 'самураи'),
        ('supernatural', 'сверхъестественное'),
        ('sport', 'спорт'),
        ('super power', 'супер сила'),
        ('horrors', 'ужасы'),
        ('fantastic', 'фантастика'),
        ('fantasy', 'фэнтези'),
        ('action', 'экшен'),
        ('etty', 'этти'),
        ('thriller', 'триллер')
    ]
    choices_max_length = MAX(choices)
    genre = models.CharField(max_length=choices_max_length, choices=choices, verbose_name='Категория',
                             default=choices[0], primary_key=True,unique=True)

    class Meta:
        ordering = ['-genre']

    def __str__(self):
        return self.get_genre_display()





class Anime(models.Model):
    choices_GENRE = [
        ('senen', 'сёнен'),
        ('senen-ai', 'сёнен-ай'),
        ('seinen', 'сэйнен'),
        ('shojo', 'сёдзё'),
        ('shojo-ai', 'сёдзё-ай'),
        ('dzesei', 'дзёсей'),
        ('comedy', 'комедия'),
        ('romance', 'романтика'),
        ('school', 'школа'),
        ('madness', 'безумие'),
        ('martial_arts', 'боевые искусства'),
        ('vampires', 'вампиры'),
        ('war', 'военное'),
        ('harem', 'гарем'),
        ('gourmet', 'гурман'),
        ('demons', 'демоны'),
        ('detective', 'детектив'),
        ('baby', 'детское'),
        ('drama', 'драма'),
        ('historical', 'исторический'),
        ('space', 'космос'),
        ('games', 'игры'),
        ('magic', 'магия'),
        ('cars', 'машины'),
        ('furs', 'меха'),
        ('music', 'музыка'),
        ('parody', 'пародия'),
        ('everyday life', 'повседневность'),
        ('police', 'полиция'),
        ('adventure', 'приключение'),
        ('psychological', 'психологическое'),
        ('work', 'работа'),
        ('samurai', 'самураи'),
        ('supernatural', 'сверхъестественное'),
        ('sport', 'спорт'),
        ('super power', 'супер сила'),
        ('horrors', 'ужасы'),
        ('fantastic', 'фантастика'),
        ('fantasy', 'фэнтези'),
        ('action', 'экшен'),
        ('etty', 'этти'),
        ('thriller', 'триллер')
    ]
    choices_TYPE = [('film', 'фильм'),
               ('series', 'сериал'),
               ('spec', 'спешл'),
               ('clip', 'клип'),
               ('ova', 'ova'),
               ('ona', 'ona')
               ]
    name = models.CharField(max_length=100, verbose_name='Название')
    status = models.CharField(max_length=choices_max_length, choices=choices, verbose_name='Статус',
                              default=choices[0][0])
    rating = models.PositiveSmallIntegerField(choices=choices_rating, verbose_name='Рэйтинг',
                                              default=choices_rating[0][0],blank=True, null=True)
    about = models.TextField(verbose_name='Описание')
    genre = MultiSelectField( verbose_name='Жанр',choices=choices_GENRE,blank=True, null=True)
    typeAnime = models.CharField(max_length=100, verbose_name='Тип',
                                  default=choices_TYPE[0][0],choices=choices_TYPE)
    trailer = models.FileField(verbose_name='Трейлер', blank=True, null=True)
    image = models.ImageField(verbose_name='Заглавная картинка', blank=True, null=True)
    links = models.TextField(verbose_name='Ссылки на источники для просмотра аниме', blank=True, null=True)

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'

    def __str__(self):
        return self.name
