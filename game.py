import arcade


class Game(arcade.Window):  # Класс отвечающий за окно
    pass


if __name__ == '__main__':
    window = Game  # Создание экземпляра класса Game
    arcade.run()  # Запуск цикла обновлений