class User:
     """
        Класс пользователя
        Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число
     """
     def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

     def __contains__(self, item):
         for user in item:
             if self.nickname == user.nickname:
                 return True
         return False


class Video:
    """
    Класс Video:
    Атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту,
    bool (False по умолчанию))
    """
    def __init__(self, title, duration, audit_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.audit_mode = audit_mode



class UrTube:

    """
    Rласс UrTube
    Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = [] # создаем список,для экземпляра
        self.videos = []
        self.current_user = 0
    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user


    def register(self, nickname, password, age):
        tem_user = User(nickname, password, age)
        if tem_user not in self.users:
            self.users.append(tem_user)
        else:
            print(f'Пользователь {tem_user.nickname} уже существует')
        self.log_in(tem_user.nickname, tem_user.password)

    def log_out(self):
        ...
    def add(self, title, duration):
        videos_ = Video(title, duration)
        if videos_ not in self.videos:
            self.videos.append(videos_)

        else:
            ...

    def get_videos(self, word):
        same_words = []
        if word.lower() in self.videos:
            same_words.append(self.videos)
        return same_words

    def watch_vedeo(self, title):
        ...



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
#print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
#
#
#
#
#
#
#
#
