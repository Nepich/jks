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
