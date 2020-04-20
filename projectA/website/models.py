from django.db import models


class Category(models.Model):
    """Категории"""
    title = models.CharField("Категория", max_length=128)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField("Название", max_length=128)
    code = models.SmallIntegerField("Код страны", default=0)
    flag = models.ImageField("Флаг", upload_to="flags/")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.title


class Actor(models.Model):
    """Актеры,  режиссеры, сценаристы и продюсеры"""
    name = models.CharField("Имя", max_length=128)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="images/")
    birthday = models.DateField("Дата рождения", default=0)
    role = models.CharField("Роль", max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = "Актер, режиссер, сценарист и продюсер"
        verbose_name_plural = "Актеры,  режиссеры, сценаристы и продюсеры"

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанры"""
    title = models.CharField("Название", max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.title


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=128)
    tagline = models.CharField("Слоган", max_length=128, default='')
    image = models.ImageField("Картина", upload_to="movies/")
    description = models.TextField("Описание")
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="movie_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="movie_actor")
    scenarist = models.ManyToManyField(Actor, verbose_name="сценарист", related_name="movie_scenarist")
    producer = models.ManyToManyField(Actor, verbose_name="продюсер", related_name="movie_producer")
    release_date = models.PositiveSmallIntegerField("Дата выхода", default=0)
    genres = models.ManyToManyField(Genre, verbose_name="жанры", related_name="movie_genre")
    total_duration = models.PositiveSmallIntegerField("Длительность", blank=True, null=True)
    country = models.ManyToManyField(Country, verbose_name="Страна", related_name="movie_country")
    budget = models.PositiveIntegerField("Бюджет", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]

    def __str__(self):
        return f'{self.value}'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=16)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return f"{self.star} - {self.movie}"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField("Email")
    name = models.CharField("Имя", max_length=128)
    text = models.TextField("Сообщение", max_length=4096)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.name} - {self.movie}"
