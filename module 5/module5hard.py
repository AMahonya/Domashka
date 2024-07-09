import time
class User:
    """
    Этот класс отвечает за создание пользователей содержащий атрибуты:
     имя пользователя, пароль(в хэшированном виде), позраст.
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(password)

    def __str__(self):
        return f"{self.nickname}"

    def __eq__(self, other):
        return self.nickname == other.nickname



class Video:
    """
    Этот класс отвечает за создание видео содержищие атрибуты:
     заголовок, продолжительность, время просмотра(остановки) , ограничение по возрасту.

    """

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    '''

    Этот класс отвечает за управление платформой UrTube. Он содержит списки пользователей и видео,
     а также текущего пользователя. Реализованы методы для входа, регистрации, выхода, добавления видео,
      поиска видео по ключевому слову и просмотра видео

    '''

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        return f"{self.videos}"

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                break
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos) -> None :
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, поэтому Вы не можете смотреть это видео.")
                    return

                start_video = input("Нажмите 'P' для старта видео: ")
                if start_video == 'P':

                    while video.time_now < video.duration:
                        print(f"{video.time_now + 1} ", end="")
                        video.time_now += 1
                        time.sleep(1)
                    video.time_now = 0
                    print("Конец видео")
                else:
                    print("Вы отказались от просмотра видео.")
                return

        print(f"Видео '{title}' не найдено.")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')