from django.db import models
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField


class Header(models.Model):
    about_us = models.CharField(max_length=100, default="О нас", verbose_name="О нас")
    projects = models.CharField(max_length=100, default="Проекты", verbose_name="Проекты")
    contacts = models.CharField(max_length=100, default="Контакты", verbose_name="Контакты")
    logo = ResizedImageField(force_format='WEBP', quality=100, upload_to='header/', verbose_name="Логотип", blank=True)

    class Meta:
        verbose_name = 'Хэдер'
        verbose_name_plural = 'Хэдер'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Хэдер'

    def logo_image(self):
        if self.logo:
            return mark_safe(f'<img src={self.logo.url} width="50" height="60"')
        else:
            return '(No image)'

    logo_image.short_description = 'Изображение'


class Footer(models.Model):
    text_us = models.CharField(max_length=100, default="Напишите нам", verbose_name="Поле напишите нам")
    interests = models.CharField(max_length=100, default="Что интересует?", verbose_name="Поле интересует")
    about_u = models.CharField(max_length=100, default="О вас", verbose_name="Поле о вас")
    company_name = models.CharField(max_length=100, default="JKS Entertainment", verbose_name="Название компании")
    company_description = models.TextField(verbose_name="Описание компании")
    tiktok_url = models.URLField(verbose_name="URL tiktoka")
    instagram_url = models.URLField(verbose_name="URL instagram")
    mail_field = models.CharField(max_length=100, verbose_name="Почта")
    contact_info = models.CharField(max_length=100, default="Контактная информация:",
                                    verbose_name="Заголовок контактной информации")
    services = models.CharField(max_length=100, default="Сервисы", verbose_name="Поле сервисы")
    about_us = models.CharField(max_length=100, default="О нас", verbose_name="Поле о нас")
    phone = models.CharField(max_length=20, verbose_name="Поле телефона")

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Футер'


class Choices(models.Model):
    type = models.CharField(max_length=100, verbose_name="Тип интереса")
    footer = models.ForeignKey(Footer, on_delete=models.SET_NULL, null=True, related_name='footer_choices')

    class Meta:
        verbose_name = 'Тип интереса'
        verbose_name_plural = 'Типы интереса'

    def __str__(self):
        return self.type


class Form(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.CharField(max_length=100, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    company = models.CharField(max_length=200, verbose_name="Компания")
    type = models.ForeignKey(Choices, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка от {self.name}'


class BasePageModel(models.Model):
    header = models.ForeignKey(Header, on_delete=models.SET_NULL, null=True, default=1, verbose_name="Хэдер")
    footer = models.ForeignKey(Footer, on_delete=models.SET_NULL, null=True, default=1, verbose_name="Футер")

    class Meta:
        abstract = True


class MainPage(BasePageModel):
    main_photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='main/',
                                   verbose_name="Фото главной страницы", blank=True)
    main_video = models.FileField(upload_to='main/', verbose_name="Видео главной страницы", blank=True)
    who_are_we = models.CharField(max_length=100, default="Кто мы?", verbose_name="Поле кто мы")
    who_are_we_desc = models.TextField(verbose_name="Кто мы описание")
    learn_more = models.CharField(max_length=100, default="Узнать больше", verbose_name="Кнопка узнать больше")
    projects = models.CharField(max_length=100, default="Проекты", verbose_name="Поле проекты")
    statistics = models.CharField(max_length=100, default="Цифры громче слов", verbose_name="Заголовок статистики")
    influencers = models.CharField(max_length=100, default="Инфлюенсеров", verbose_name="Заголовок инфлюенсеров")
    influencers_info = models.CharField(max_length=100, default="25+", verbose_name="Значение инфлюенсеров")
    subscribers = models.CharField(max_length=100, default="Подписчиков", verbose_name="Заголовок подписчиков")
    subscribers_info = models.CharField(max_length=100, default="200м+", verbose_name="Значение подписчиков")
    likes = models.CharField(max_length=100, default="Лайков в тиктоке", verbose_name="Заголовок лайков")
    likes_info = models.CharField(max_length=100, default="5млрд+", verbose_name="Значение лайков")
    views = models.CharField(max_length=100, default="Просмотров в месяц", verbose_name="Заголовок просмотров")
    views_info = models.CharField(max_length=100, default="1млрд", verbose_name="Значение просмотров")
    partners = models.CharField(max_length=100, default="Партнеры", verbose_name="Заголовок партнеры")

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Главная страница'

    def main_photo_image(self):
        if self.main_photo:
            return mark_safe(f'<img src={self.main_photo.url} width="50" height="60"')
        else:
            return '(No image)'

    main_photo_image.short_description = 'Изображение'


class Partner(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name="Название партнера")
    partner_logo = ResizedImageField(force_format='WEBP', quality=100, upload_to='partner/',
                                     verbose_name="Лого партнера")
    page = models.ForeignKey(MainPage, on_delete=models.SET_NULL, null=True, default=1,
                             related_name='main_page_partners')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return f'Партнер {self.name}'

    def logo_image(self):
        if self.partner_logo:
            return mark_safe(f'<img src={self.partner_logo.url} width="50" height="60"')
        else:
            return '(No image)'

    logo_image.short_description = 'Изображение'


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя проекта")
    description = models.TextField(verbose_name="Описание проекта")
    projects_foto = ResizedImageField(force_format='WEBP', quality=100, upload_to='projects/',
                                      verbose_name="Фото проекта", blank=True)
    projects_video = models.FileField(upload_to='projects/')
    main_page = models.ForeignKey(MainPage, on_delete=models.SET_NULL, null=True, related_name='main_page_projects')
    project_page = models.ForeignKey('ProjectsPage', on_delete=models.SET_NULL, null=True,
                                     related_name='project_page_projects')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'Проект {self.name}'

    def projects_foto_image(self):
        if self.projects_foto:
            return mark_safe(f'<img src={self.projects_foto.url} width="50" height="60"')
        else:
            return '(No image)'

    projects_foto_image.short_description = 'Изображение'


class VideoProductionPage(BasePageModel):
    title = models.CharField(max_length=100, default="Видеопродакшн", verbose_name="Заголовок страницы")
    what_we_filming = models.CharField(max_length=100, default="Что мы снимаем",
                                       verbose_name="Заголовок что мы снимаем")
    first_product = models.CharField(max_length=100, default="Видео для социальных сетей",
                                     verbose_name="Заголовок первой услуги")
    first_product_desc = models.TextField(verbose_name="Описание первой услуги")
    second_product = models.CharField(max_length=100, default="Среднемасштабный продакшн",
                                      verbose_name="Заголовок первой услуги")
    second_product_desc = models.TextField(verbose_name="Описание первой услуги")
    third_product = models.CharField(max_length=100, default="Крупномасштабный продакшн",
                                     verbose_name="Заголовок первой услуги")
    third_product_desc = models.TextField(verbose_name="Описание первой услуги")
    fourth_product = models.CharField(max_length=100, default="Анимация (CGI)",
                                      verbose_name="Заголовок первой услуги")
    fourth_product_desc = models.TextField(verbose_name="Описание первой услуги")
    offer = models.TextField(verbose_name="Предложение")

    class Meta:
        verbose_name = 'Страница "Видеопродакшн"'
        verbose_name_plural = 'Страница "Видеопродакшн"'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Страница "Видеопродакшн"'


class Content(models.Model):
    page = models.ForeignKey(VideoProductionPage, on_delete=models.SET_NULL, null=True, related_name='page_content',
                             default=1)
    content_photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='main/',
                                      verbose_name="Фото для страницы видеопродакшн")
    content_video = models.FileField(upload_to='video_prod_cont/', default=None, blank=True, null=True,
                                     verbose_name="Видео для страницы видеопродакшн")

    class Meta:
        verbose_name = 'Контент страницы видеопродакшн'
        verbose_name_plural = 'Контент страницы видеопродакшн'

    def content_photo_image(self):
        if self.content_photo:
            return mark_safe(f'<img src={self.content_photo.url} width="50" height="60"')
        else:
            return '(No image)'

    content_photo_image.short_description = 'Изображение'


class AboutUsPage(BasePageModel):
    title = models.CharField(max_length=255, default="ВАЙНЕРЫ? УЖЕ НЕТ. JKS- ЭТО МЕДИАКОМПАНИЯ.",
                             verbose_name="Заголовок страницы о нас")
    first_text = models.TextField(verbose_name="Первый текст")
    second_text = models.TextField(verbose_name="Второй текст")
    third_text = models.TextField(verbose_name="Третий текст")
    fourth_text = models.TextField(verbose_name="Четвертый текст")
    fifth_text = models.TextField(verbose_name="Пятый текст")
    sixth_text = models.TextField(verbose_name="Шестой текст")
    seventh_text = models.TextField(verbose_name="Седьмой текст")
    eighth_text = models.TextField(verbose_name="Восьмой текст")
    photo_background1 = ResizedImageField(quality=100, upload_to='about_us/',
                                          verbose_name="Фото подложки 1", blank=True)
    photo_background2 = ResizedImageField(quality=100, upload_to='about_us/',
                                          verbose_name="Фото подложки 2", blank=True)
    photo_background3 = ResizedImageField(quality=100, upload_to='about_us/',
                                          verbose_name="Фото подложки 3", blank=True)
    photo_background4 = ResizedImageField(quality=100, upload_to='about_us/',
                                          verbose_name="Фото подложки 4", blank=True)
    photo_background5 = ResizedImageField(quality=100, upload_to='about_us/',
                                          verbose_name="Фото подложки 5", blank=True)
    photo_background6 = ResizedImageField(quality=100, upload_to='about_us/',
                                          verbose_name="Фото подложки 6", blank=True)

    class Meta:
        verbose_name = 'Страница "О нас"'
        verbose_name_plural = 'Страница "О нас"'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Страница "О нас"'


class People(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=255, verbose_name="Должность")
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='about_us/', verbose_name="Фото человека",
                              blank=True)
    page = models.ForeignKey(AboutUsPage, on_delete=models.SET_NULL, null=True, default=1,
                             related_name='about_us_people')

    class Meta:
        verbose_name = 'Люди страницы "О нас"'
        verbose_name_plural = 'Люди страницы "О нас"'

    def __str__(self):
        return f'Человек {self.name}'

    def photo_image(self):
        if self.photo:
            return mark_safe(f'<img src={self.photo.url} width="50" height="60"')
        else:
            return '(No image)'

    photo_image.short_description = 'Изображение'


class ProjectsPage(BasePageModel):
    title = models.CharField(max_length=255, default="Проекты", verbose_name="Заголовок страницы проекты")

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страница "Проекты"'
        verbose_name_plural = 'Страница "Проекты"'

    def __str__(self):
        return 'Страница "Проекты"'


class InfluencersPage(BasePageModel):
    title = models.CharField(max_length=255, default="Инфлюенсеры", verbose_name="Заголовок страницы инфлюенсеры")
    first_text = models.CharField(max_length=255, default="Крупнейшие TikTok-хаусы и лучшие блогеры",
                                  verbose_name="Первый текст")
    second_text = models.CharField(max_length=255, default="Более 300 млн подписчиков", verbose_name="Второй текст")
    third_text = models.CharField(max_length=255, default="6 серебряных и 2 золотых кнопки YouTube",
                                  verbose_name="Третий текст")

    class Meta:
        verbose_name = 'Страница "Инфлюенсеры"'
        verbose_name_plural = 'Страница "Инфлюенсеры"'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Страница "Инфлюенсеры"'


class Influencer(BasePageModel, models.Model):
    logo = ResizedImageField(force_format='WEBP', quality=100, blank=True, upload_to='influencer/',
                             verbose_name="Логотип инфлюенсера/дома")
    name = models.CharField(max_length=100, default="", verbose_name="Имя/название дома")
    statistics = models.CharField(max_length=100, default="Статистика", verbose_name="Заголовок блока статистика")
    instagram_statistics = models.CharField(max_length=100, default="В instagram",
                                            verbose_name="Заголовок статистика инстаграм", blank=True)
    instagram = models.CharField(max_length=100, verbose_name="Статистика инстаграм", blank=True)
    tiktok_statistics = models.CharField(max_length=100, default="В tiktok", verbose_name="Заголовок статистика tiktok",
                                         blank=True)
    tiktok = models.CharField(max_length=100, verbose_name="Статистика tiktok", blank=True)
    youtube_statistics = models.CharField(max_length=100, default="В youtube",
                                          verbose_name="Заголовок статистика youtube", blank=True)
    youtube = models.CharField(max_length=100, verbose_name="Статистика youtube", blank=True)
    description = models.TextField(verbose_name="Описание инфлюенсера/дома", blank=True)
    page = models.ForeignKey(InfluencersPage, default=1, on_delete=models.CASCADE, related_name='influencer')

    class Meta:
        verbose_name = 'Страница инфлюенсера/тик-ток дома'
        verbose_name_plural = 'Страницы инфлюенсера/тик-ток дома'

    def __str__(self):
        return f'Инфлюенсер/дом {self.name}'


class InfluncerPhoto(models.Model):
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='influencer/',
                              verbose_name="Фото инфлюенсера")
    description = models.TextField(verbose_name="Описание под фото")
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, verbose_name="Отношение к инфлюенсеру",
                                   related_name='influencer_photo')

    class Meta:
        verbose_name = 'Фото инфлюенсера'
        verbose_name_plural = 'Фото инфлюенсера'

    def __str__(self):
        return f'Фото инфлюенсера {self.influencer.name}'

    def photo_image(self):
        if self.photo:
            return mark_safe(f'<img src={self.photo.url} width="50" height="60"')
        else:
            return '(No image)'


class InfluencerMembers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя участника дома")
    instagram_statistics = models.CharField(max_length=100, default="В instagram",
                                            verbose_name="Заголовок статистика инстаграм", blank=True)
    instagram = models.CharField(max_length=100, verbose_name="Статистика инстаграм", blank=True)
    tiktok_statistics = models.CharField(max_length=100, default="В tiktok",
                                         verbose_name="Заголовок статистика tiktok", blank=True)
    tiktok = models.CharField(max_length=100, verbose_name="Статистика tiktok", blank=True)
    youtube_statistics = models.CharField(max_length=100, default="В youtube",
                                          verbose_name="Заголовок статистика youtube", blank=True)
    youtube = models.CharField(max_length=100,  verbose_name="Статистика youtube", blank=True)
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='influencer/',
                              verbose_name="Фото участника дома")
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, verbose_name="Отношение к дому",
                                   related_name='influencer_member')

    class Meta:
        verbose_name = 'Инфо участника дома'
        verbose_name_plural = 'Инфо участников дома'

    def __str__(self):
        return f'Фото участника дома {self.influencer.name}'

    def photo_image(self):
        if self.photo:
            return mark_safe(f'<img src={self.photo.url} width="50" height="60"')
        else:
            return '(No image)'


class DubStudioPage(BasePageModel):
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='dub_studio/',
                              verbose_name="Фото страницы студия дубляжа", blank=True)
    video = models.FileField(upload_to='dub_studio/', verbose_name="Видео страницы студия дубляжа", blank=True)
    first_text = models.CharField(max_length=100, verbose_name="Первый заголовок")
    first_text_desc = models.TextField(verbose_name="Первое описание")
    second_text = models.CharField(max_length=100,  verbose_name="Второй заголовок")
    second_text_desc = models.TextField(verbose_name="Второе описание")
    third_text = models.CharField(max_length=100, verbose_name="Третий заголовок")
    third_text_desc = models.TextField(verbose_name="Третье описание")
    projects = models.CharField(max_length=100, default="Работы", verbose_name="Заголовок работы")

    class Meta:
        verbose_name = 'Страница "Студия дубляжа"'
        verbose_name_plural = 'Страница "Студия дубляжа"'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Страница "Студия дубляжа"'


class BaseDubProjects(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название проекта")
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='dub_projects/', verbose_name="Фото проекта",
                              blank=True)
    preview = models.FileField(upload_to='dub_projects/', verbose_name="Превью проекта", blank=True)
    dub_language = models.CharField(max_length=255, default="Язык дубляжа: ", verbose_name="Язык дубляжа")
    translated_by = models.CharField(max_length=100, default="Перевели: ", verbose_name="Кто перевел")
    button = models.CharField(max_length=100, default="Смотреть сейчас", verbose_name="Текст кнопки")
    url = models.URLField(verbose_name="Ссылка на проект")

    class Meta:
        abstract = True

    def __str__(self):
        return f'Проект {self.name}'

    def photo_image(self):
        if self.photo:
            return mark_safe(f'<img src={self.photo.url} width="50" height="60"')
        else:
            return '(No image)'


class DubMovies(BaseDubProjects):
    duration = models.CharField(max_length=100, default="Длительность: ", verbose_name="Длительность")
    page = models.ForeignKey(DubStudioPage, on_delete=models.CASCADE, related_name='movie_projects')

    class Meta:
        verbose_name = 'Дублированный фильм/мультфильм'
        verbose_name_plural = 'Дублированные фильмы/мультфильмы'


class DubSeries(BaseDubProjects):
    total_series = models.CharField(max_length=100, default="Всего серий: ", verbose_name="Всего серий")
    dub_series = models.CharField(max_length=100, default="Озвучено: ", verbose_name="Озвучено")
    page = models.ForeignKey(DubStudioPage, on_delete=models.CASCADE, related_name='series_projects')

    class Meta:
        verbose_name = 'Дублированный сериал/мультсериал'
        verbose_name_plural = 'Дублированные сериалы/мультсериалы'


class Studio(models.Model):
    logo = ResizedImageField(force_format='WEBP', quality=100, upload_to='dub_studio/', verbose_name="Логотип студии",
                             blank=True)
    name = models.CharField(max_length=100, default="", verbose_name="Название студии")
    page = models.ForeignKey(DubStudioPage, on_delete=models.CASCADE, related_name='studio')

    class Meta:
        verbose_name = 'Студия дубляжа'
        verbose_name_plural = 'Студии дубляжа'

    def __str__(self):
        return f'Студия {self.name}'


class Voice(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя переводившего")
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='dub_studio/',
                              verbose_name="Фото переводившего", blank=True)
    voice = models.FileField(upload_to='dub_studio/', verbose_name="Запись голоса", blank=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, verbose_name="Отношение к студии",
                               related_name='voice')

    class Meta:
        verbose_name = 'Голос студии дубляжа'
        verbose_name_plural = 'Голоса студии дубляжа'

    def __str__(self):
        return f'Голос {self.name}'

    def photo_image(self):
        if self.photo:
            return mark_safe(f'<img src={self.photo.url} width="50" height="60"')
        else:
            return '(No image)'


class AnimationStudioPage(BasePageModel):
    title = models.CharField(max_length=100, default="Студия анимации",
                             verbose_name="Заголовок страницы студия анимации")
    field = models.CharField(max_length=100, default="Coming soon", verbose_name="Заглушка")

    class Meta:
        verbose_name = 'Страница "Студия анимации"'
        verbose_name_plural = 'Страница "Студия анимации"'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Страница "Студия анимации"'


class SeriesFilmsPage(BasePageModel):
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='series/',
                              verbose_name="Изображение страницы", blank=True)
    title = models.CharField(max_length=100, default="Королева двора", verbose_name="Заголовок проекта")
    description = models.TextField(verbose_name="Описание проекта")
    projects = models.CharField(max_length=100, default="Работы", verbose_name="Заголовок работы")

    class Meta:
        verbose_name = 'Страница "Сериалы-фильмы"'
        verbose_name_plural = 'Страница "Сериалы-фильмы"'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Страница "Сериалы-фильмы"'


class SeriesFilms(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название проекта")
    age = models.CharField(max_length=100, default="Возраст: ", verbose_name="Возраст")
    series_number = models.CharField(max_length=100, default="Кол-во серий: ", verbose_name="Кол-во серий")
    language = models.CharField(max_length=100, default="Язык: ", verbose_name="Язык")
    genre = models.CharField(max_length=100, default="Жанр: ", verbose_name="Жанр")
    button = models.CharField(max_length=100, default="Смотреть сейчас", verbose_name="Кнопка смотреть сейчас")
    url = models.URLField(verbose_name="Ссылка на проект")
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='series/', verbose_name="Фото проекта",
                              null=True, blank=True)
    preview = models.FileField(upload_to='series/', verbose_name="Превью проекта", null=True, blank=True)
    page = models.ForeignKey(SeriesFilmsPage, on_delete=models.CASCADE, related_name='series_films')

    class Meta:
        verbose_name = 'Сериал/фильм'
        verbose_name_plural = 'Сериалы/фильмы'

    def __str__(self):
        return f'Проект {self.name}'

    def photo_image(self):
        if self.photo:
            return mark_safe(f'<img src={self.photo.url} width="50" height="60"')
        else:
            return '(No image)'


class GameDevPage(BasePageModel):
    title = models.CharField(max_length=255, default="Разработка игр", verbose_name="Заголовок страницы разработка игр")
    first_text = models.CharField(max_length=100, verbose_name="Первый заголовок")
    first_text_desc = models.TextField(verbose_name="Первое описание")
    second_text = models.CharField(max_length=100, verbose_name="Второй заголовок")
    second_text_desc = models.TextField(verbose_name="Второе описание")
    photo_background1 = ResizedImageField(quality=100, upload_to='game_dev/', verbose_name="Фото подложки 1",
                                          blank=True)
    photo_background2 = ResizedImageField(quality=100, upload_to='game_dev/', verbose_name="Фото подложки 2",
                                          blank=True)
    photo_background3 = ResizedImageField(quality=100, upload_to='game_dev/', verbose_name="Фото подложки 3",
                                          blank=True)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страница "Разработка игр"'
        verbose_name_plural = 'Страница "Разработка игр"'

    def __str__(self):
        return 'Страница "Разработка игр"'


class Game(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name="Название игры")
    photo = ResizedImageField(force_format='WEBP', quality=100, upload_to='gamedev/', verbose_name="Изображение игры",
                              blank=True)
    statistics = models.CharField(max_length=100, default="Статистика ", verbose_name="Заголовок статистики")
    ios_statistics = models.CharField(max_length=100, verbose_name="IOS статистика", blank=True)
    ios = models.CharField(max_length=100, default="на ios", verbose_name="Заголовок IOS статистики")
    android_statistics = models.CharField(max_length=100, verbose_name="Android статистика", blank=True)
    android = models.CharField(max_length=100, default="на android", verbose_name="Заголовок Android статистики")
    title = models.CharField(max_length=100, default="Найди каждому пару", verbose_name="Заголовок ссылок")
    appstore_url = models.URLField(verbose_name="Ссылка на проект в AppStore")
    googleplay_url = models.URLField(verbose_name="Ссылка на проект в GooglePlay")
    page = models.ForeignKey(GameDevPage, on_delete=models.CASCADE, related_name='games', null=True, blank=True)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return f'Проект {self.name}'

    def photo_image(self):
        if self.photo:
            return mark_safe(f'<img src={self.photo.url} width="50" height="60"')
        else:
            return '(No image)'


class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя менеджера")
    email = models.CharField(max_length=100, verbose_name="Email для отправки писем")

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        return f'Менеджер {self.name}'
