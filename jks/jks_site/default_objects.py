from django.apps import apps


def create_default_header():
    header = apps.get_model(app_label='jks_site', model_name='Header')
    data = {'about_us': 'О нас',
            'projects': 'Проекты',
            'contacts': 'Контакты'}
    header.objects.create(**data)


def create_default_footer():
    footer = apps.get_model(app_label='jks_site', model_name='Footer')
    data = {'text_us': 'Напишите нам',
            'interests': 'Что интересует?',
            'about_u': 'О вас',
            'company_name': 'JKS Entertainment',
            'company_description': 'JSK Entertainment – медиа компания, создающая контент для диджитал платформ и '
                                   'социальных сетей.',
            'tiktok_url': 'https://www.tiktok.com/',
            'instagram_url': 'https://www.instagram.com/',
            'mail_field': 'bloggers@jks.kz',
            'contact_info': 'Контактная информация:',
            'services': 'Сервисы',
            'about_us': 'О нас',
            'phone': '+7 (777) 112 20 50'}
    footer.objects.create(**data)


def create_default_choices():
    choices = apps.get_model(app_label='jks_site', model_name='Choices')
    data = [
        {'type': 'Инфлюенсеры', 'footer': '1'},
        {'type': 'Продакшн', 'footer': '1'},
        {'type': 'Анимация', 'footer': '1'},
        {'type': 'Дубляж', 'footer': '1'},
        {'type': 'Разработка игр', 'footer': '1'},
    ]
    [choices.objects.create(**obj) for obj in data]


def create_default_main_page():
    main_page = apps.get_model(app_label='jks_site', model_name='MainPage')
    data = {'header': '1', 'footer': '1',
            'who_are_we': 'Кто мы?',
            'who_are_we_desc': 'Мы – диджитал, о котором говорят. Мы создаём, снимаем, продвигаем, разрабатываем и '
                               'озвучиваем контент с виральными медиапоказателями.',
            'learn_more': 'Узнать больше',
            'projects': 'Проекты',
            'statistics': 'Цифры громче слов',
            'influencers': 'Инфлюенсеров',
            'influencers_info': '25+',
            'subscribers': 'Подписчиков',
            'subscribers_info': '200М+',
            'likes': 'Лайков в тиктоке',
            'likes_info': '5МЛРД+',
            'views': 'Просмотров в месяц',
            'views_info': '1млрд',
            'partners': 'Партнеры'}
    main_page.objects.create(**data)


def create_default_projects():
    project = apps.get_model(app_label='jks_site', model_name='Project')
    data = [{'name': 'Продакшн',
             'description': 'От раскадровки до постпродакшена. Любого уровня сложности, масштаба и графики.',
             'main_page': '1',
             'project_page': '1'},
            {'name': 'Инфлюенсеры',
             'description': 'Наши блогеры и TikTok-хаусы для ваших будущих коллабораций.',
             'main_page': '1',
             'project_page': '1'},
            {'name': 'Студия Дубляжа',
             'description': 'Популярные фильмы, аниме и сериалы теперь звучат на казахском!',
             'main_page': '1',
             'project_page': '1'},
            {'name': 'Сериалы-фильмы',
             'description': 'Сценарии, которые оживают на экранах и находят славу за рубежом.',
             'main_page': '1',
             'project_page': '1'},
            {'name': 'Студия анимации',
             'description': 'Магия создания 2D и 3D. Вжух!',
             'main_page': '1',
             'project_page': '1'},
            {'name': 'Разработка игр',
             'description': 'Любимые блогеры в мобильном телефоне ',
             'main_page': '1',
             'project_page': '1'},
            ]
    [project.objects.create(**obj) for obj in data]


def create_default_projects_page():
    projects_page = apps.get_model(app_label='jks_site', model_name='ProjectsPage')
    data = {'header': '1', 'footer': '1', 'title': 'Проекты'}
    projects_page.objects.create()


def create_default_video_product_page():
    video_product_page = apps.get_model(app_label='jks_site', model_name='VideoProductionPage')
    data = {
        'header': '1', 'footer': '1',
        'title': 'Видеопродакшн',
        'what_we_filming': 'Что мы снимаем?',
        'first_product': 'Видео для социальных сетей',
        'first_product_desc': 'Видео в социальных сетях сейчас в тренде, и мы можем помочь рассказать вашу историю на '
                              'каждой платформе в Instagram, TikTok. Дополнительно возможна адаптация ролика для '
                              'Youtube.',
        'second_product': 'Среднемасштабный продакшн',
        'second_product_desc': 'Упрощенный вариант продакшна который подходит для оптимизации бюджета. Производство '
                               'видео контента под ключ.',
        'third_product': 'Крупномасштабный продакшн',
        'third_product_desc': 'Продакшн полного цикла, с привлечением топовых узконаправленных специалистов. '
                              'Производство видео контента (рекламных роликов) под ключ, который можно использовать '
                              'на телевидение, социальных сетях и видеохостинге.',
        'fourth_product': '',
        'fourth_product_desc': 'Анимация выводит нас из реального мира и помогает рассказывать большие истории. Мы '
                               'можем помочь вам объяснить сложный продукт или услугу с помощью наших привлекательных '
                               'анимационных видеороликов. Мы готовы предложить вам производство полноценного '
                               'анимационного ролика (состоящего полностью из CGI)',
        'offer': 'Если вам интересно как это все происходит, то пишите нам, мы вас проконсультируем!'
    }
    video_product_page.objects.create(**data)


def create_default_about_us_page():
    about_us_page = apps.get_model(app_label='jks_site', model_name='VideoProductionPage')
    data = {
        'header': '1', 'footer': '1',
        'title': 'ВАЙНЕРЫ? УЖЕ НЕТ. JKS- ЭТО МЕДИАКОМПАНИЯ.',
        'first_text': 'Вы делились с друзьями скетчами Jokeasses и пели вместе с нами «зын-зын». Но мы идём дальше.',
        'second_text': 'Сейчас JKS – крупная медиакомпания с командой профессионалов.',
        'third_text': 'Cоздаём лучших TikTok’еров и TikTok-хаусы',
        'fourth_text': 'Снимаем рекламу для мировых брендов и лейблов',
        'fifth_text': 'Владеем искусством CGI',
        'sixth_text': 'Дублируем фильмы и сериалы на казахский',
        'seventh_text': 'Разрабатываем мобильные игры',
        'eighth_text': 'И это далеко не всё. Лучше всего о нас скажут наши проекты',
    }
    about_us_page.objects.create(**data)


def create_default_people():
    people = apps.get_model(app_label='jks_site', model_name='People')
    data = [
        {
            'name': 'Асхат Халимов',
            'position': 'Основатель и продюсер BIP House',
            'page': '1',
        },
        {
            'name': 'Бексултан Казыбек',
            'position': 'Главный продюсер',
            'page': '1',
        },
        {
            'name': 'Азат Халимов',
            'position': 'Основатель и продюсер Yolo House',
            'page': '1',
        }
    ]
    [people.objects.create(**obj) for obj in data]


def create_default_influencers_page():
    influencers_page = apps.get_model(app_label='jks_site', model_name='VideoProductionPage')
    data = {
        'header': '1', 'footer': '1',
        'title': 'ИНФЛЮЕНСЕРЫ',
        'first_text': 'Крупнейшие TikTok-хаусы и лучшие блогеры',
        'second_text': 'Более 300 млн подписчиков',
        'third_text': '6 серебряных и 2 золотых кнопки YouTube'
    }
    influencers_page.objects.creeate(**data)


def create_default_influencer():
    influencer = apps.get_model(app_label='jks_site', model_name='Influencer')
    data = [
        {
            'header': '1', 'footer': '1',
            'name': 'Yolo House',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '1M',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '26M',
            'youtube_statistics': 'В youtube',
            'youtube': '3.45K',
            'description': 'Казахстанский TikTok-хаус, который за год своего существования стал САМЫМ ПОПУЛЯРНЫМ ДОМОМ В '
                           'МИРЕ. В принципе, это всё, что нужно знать. Ну, ещё о его участниках. ',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'BIP House',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '667K',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '24.5M',
            'youtube_statistics': 'В youtube',
            'youtube': '2.3M',
            'description': 'Bangers in Pyjamas – самый первый TikTok-хаус в Казахстане, занявший 3-е место по '
                           'количеству подписчиков в мире. Они живут в одном особняке и устраивают движ. У них есть '
                           'армия фанатов и премия от Nickelodeon.',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'Satori',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '104K',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '228K',
            'youtube_statistics': '',
            'youtube': '',
            'description': '',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'HOMM9K',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '2M',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '44M',
            'youtube_statistics': '986K',
            'youtube': 'В youtube',
            'description': 'Алина Ким, а лучше Хомяк, а ещё лучше Хома – топ 1 TikTok’ер в СНГ. Суперсила: '
                           'бесконечный позитив и чутьё на тренды. Хома всегда готова к авантюрам, особенно если '
                           'нужно танцевать, сменить образ или стать новым хокаге.',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'Aminka Vitaminka',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '1.3M',
            'tiktok_statistics': '',
            'tiktok': '',
            'youtube_statistics': 'В youtube',
            'youtube': '5.44M',
            'description': 'Возраст – не помеха, если ты звезда. Наша маленькая Амина успешно покоряет сердца '
                           'медиапространства и не собирается останавливаться. В чём секрет? Если есть харизма и '
                           'искренность, промахнуться невозможно.',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'Ariokka',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '227K',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '472K',
            'youtube_statistics': '',
            'youtube': '',
            'description': 'Мама Аминки Витаминки, и двух талантливых девочек – Адёки, Аружан и маленького Амира. '
                           'Сценарист, режиссёр, оператор, монтажёр, PR-агент и генератор идей для каналов детей. В '
                           'общем – чудо-женщина с надёжной помощью от мужа.',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'HAAJEE_NAIMAN',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '207K',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '103K',
            'youtube_statistics': '',
            'youtube': '',
            'description': 'Аджибола Аканни – африканец, живущий в Казахстане. Он преподаёт английский язык в школе, '
                           'сам учит казахский и играет в футбол. Аджи снимает ролики, где с юмором рассказывает о '
                           'жизни иностранца в Казахстане.',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'Dovetail',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '207K',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '103K',
            'youtube_statistics': '',
            'youtube': '',
            'description': '',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'Rendi',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '207K',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '103K',
            'youtube_statistics': '',
            'youtube': '',
            'description': '',
            'page': '1'
        },
        {
            'header': '1', 'footer': '1',
            'name': 'Mr.boom',
            'statistics': 'Статистика',
            'instagram_statistics': 'В instagram',
            'instagram': '207K',
            'tiktok_statistics': 'В tiktok',
            'tiktok': '103K',
            'youtube_statistics': '',
            'youtube': '',
            'description': '',
            'page': '1'
        },
    ]
    [influencer.objects.create(**obj) for obj in data]


def create_default_dub_studio_page():
    dub_studio_page = apps.get_model(app_label='jks_site', model_name='DubStudioPage')
    data = {
        'header': '1', 'footer': '1',
        'first_text': 'Мы хотим, чтобы любимые фильмы, аниме и сериалы звучали на казахском языке.',
        'first_text_desc': 'Поэтому наши студии подходят к озвучке профессионально и махаббатпен ❤️',
        'second_text': '«Рик и Морти» для компании «Кинопоиск»',
        'second_text_desc': 'Напрямую с англ. Без цензуры. Вы в деле?',
        'third_text': 'Если вы искали аниме на казахском языке – это здесь.',
        'third_text_desc': 'Молодые и амбициозные ребята из разных городов покажут, как бороться с Титанами, '
                           'и как звучит даттебайо по-казахски!',
        'projects': 'Работы'
    }
    dub_studio_page.oblects.create(**data)


def create_default_dub_movies():
    dub_movies = apps.get_model(app_label='jks_site', model_name='DubMovies')
    data = [
        {
            'name': 'Твоё имя',
            'dub_language': 'Язык дубляжа: Казахский',
            'translated_by': 'Перевели: Dopamine',
            'button': 'Смотреть сейчас',
            'url': 'https://www.kinopoisk.ru/film/958722/',
            'duration': 'Длительность: 1 час, 32 мин',
            'page': '1'
        },
        {
            'name': 'Ходячий Замок',
            'dub_language': 'Язык дубляжа: Казахский',
            'translated_by': 'Перевели: Dopamine',
            'button': 'Смотреть сейчас',
            'url': 'https://www.kinopoisk.ru/film/49684/',
            'duration': 'Длительность: 1 час, 59 мин',
            'page': '1'
        },
    ]
    [dub_movies.objects.create(**obj) for obj in data]


def create_default_dub_series():
    dub_series = apps.get_model(app_label='jks_site', model_name='DubSeries')
    data = [
        {
            'name': 'Рик и Морти',
            'dub_language': 'Язык дубляжа: Казахский',
            'translated_by': 'Перевели: Gur Gur Studio',
            'button': 'Смотреть сейчас',
            'url': 'https://www.kinopoisk.ru/series/685246/',
            'total_series': 'Всего серий: 4 сезона, 72 серии',
            'dub_series': 'Озвучено: 2 сезона 4 серии, 26 серий',
            'page': '1'
        },
        {
            'name': 'Атака Титантов',
            'dub_language': 'Язык дубляжа: Казахский',
            'translated_by': 'Перевели: Dopamine',
            'button': 'Смотреть сейчас',
            'url': 'https://www.kinopoisk.ru/series/749374/',
            'total_series': 'Всего серий: 4 сезона, 72 серии',
            'dub_series': 'Озвучено: 1 сезон 10 серий / 26',
            'page': '1'
        },
    ]
    [dub_series.objects.create(**obj) for obj in data]


def create_default_studio():
    dub_studio = apps.get_model(app_label='jks_site', model_name='Studio')
    data = [
        {
            'name': 'Gur Gur Studio',
            'page': '1'
        },
        {
            'name': 'Dopamine',
            'page': '1'
        }
    ]
    [dub_studio.objects.create(**obj) for obj in data]


def create_default_voices():
    voice = apps.get_model(app_label='jks_site', model_name='Voice')
    data = [
        {
            'name': 'Рик',
            'studio': '1'
        },
        {
            'name': 'Морти',
            'studio': '1'
        },
        {
            'name': 'Бет',
            'studio': '1'
        },
        {
            'name': 'Камила',
            'studio': '2'
        },
        {
            'name': 'Марлен',
            'studio': '2'
        },
        {
            'name': 'Елжас',
            'studio': '2'
        },
        {
            'name': 'Адильжан',
            'studio': '2'
        },
    ]
    [voice.objects.create(**obj) for obj in data]


def create_default_animation_studio_page():
    animation_studio_page = apps.get_model(app_label='jks_site', model_name='AnimationStudioPage')
    data = {
        'header': '1', 'footer': '1',
        'title': 'Студия анимации',
        'field': 'Coming soon'
    }
    animation_studio_page.oblects.create(**data)


def create_default_series_films_page():
    series_films_page = apps.get_model(app_label='jks_site', model_name='SeriesFilmsPage')
    data = {
        'header': '1', 'footer': '1',
        'title': 'Королева двора',
        'description': 'Девочка Аминка с сестренками переезжает в новый двор, и понимает, что территория принадлежит '
                       'местному «королю» Руслану, который установил свои правила. Тогда Амина выдает себя за '
                       '«Королеву Далекого Далекого Двора» и бросает Руслану вызов. Теперь за претендентами на '
                       'престол завязывается борьба в виде королевских состязаний.',
        'projects': 'Работы'
    }
    series_films_page.oblects.create(**data)


def create_default_series_films():
    series_films = apps.get_model(app_label='jks_site', model_name='SeriesFilms')
    data = {
        'name': 'Королева двора',
        'age': 'Возраст: 0+',
        'series_number': 'Кол-во серий: 10',
        'language': 'Язык: Русский',
        'genre': 'Жанр: Комедия',
        'button': 'Смотреть сейчас',
        'url': 'https://www.kinopoisk.ru/series/5233488/',
        'page': '1'
    }
    series_films.oblects.create(**data)


def create_default_game_dev_page():
    game_dev_page = apps.get_model(app_label='jks_site', model_name='GameDevPage')
    data = {
        'header': '1', 'footer': '1',
        'title': 'Разработка игр',
        'first_text': 'Мы не только любим игры, но и разрабатываем их.',
        'first_text_desc': 'Управляйте и прокачивайте любимых блогеров в BIP HOUSE Ride или же находите им пару и '
                           'развивайте отношения в Yolo Run.',
        'second_text': 'Хотите создать успешную мобильную игру? вам к нам',
        'second_text_desc': 'Простая механика, увлекательный геймплей и яркая графика — основные критерии разработки.'
    }
    game_dev_page.oblects.create(**data)


def create_default_game():
    game = apps.get_model(app_label='jks_site', model_name='Game')
    data = [
        {
            'name': 'YoloRun',
            'statistics': 'Cтатистика ',
            'ios_statistics': '1.8M',
            'ios': 'на ios',
            'android_statistics': '356K',
            'android': 'на android',
            'title': 'Найди каждому пару',
            'appstore_url': 'https://apps.apple.com/ru/app/yolo-run/id1582190271?l=en',
            'googleplay_url': 'https://play.google.com/store/apps/details?id=com.PimpochkaGames.YoloRun&hl=ru&gl=US',
            'page': '1'
        },
        {
            'name': 'BipHouseRide',
            'statistics': 'Cтатистика ',
            'ios_statistics': '',
            'ios': 'на ios',
            'android_statistics': '',
            'android': 'на android',
            'title': 'Найди каждому пару',
            'appstore_url': 'https://apps.apple.com/kz/app/bip-house-ride/id1635620022',
            'googleplay_url': 'https://play.google.com/store/apps/details?id=com.PimpochkaGames.BipHouseRide&hl=ru&gl'
                              '=US',
            'page': '1'
        }
    ]


def create_default_objects():
    create_default_header()
    create_default_footer()
    create_default_choices()
    create_default_main_page()
    create_default_video_product_page()
    create_default_about_us_page()
    create_default_people()
    create_default_projects_page()
    create_default_projects()
    create_default_influencers_page()
    create_default_influencer()
    create_default_dub_studio_page()
    create_default_dub_movies()
    create_default_dub_series()
    create_default_studio()
    create_default_voices()
    create_default_animation_studio_page()
    create_default_series_films_page()
    create_default_series_films()
    create_default_game_dev_page()
    create_default_game()
