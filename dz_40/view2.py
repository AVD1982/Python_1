class UserInterface:

    def wait_user_answer(self):
        print(" Редактирование данных каталога фильмов ".center(50, '='))
        print("Действия с Фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        print('=' * 50)
        return user_answer

    def add_user_aticle(self):
        dict_article = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        print(" Создание фильма: ".center(50, '='))
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} : ')
        print('=' * 50)
        return dict_article
