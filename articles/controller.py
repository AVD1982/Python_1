from view import UserInterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.arcticle_model = ArticleModel()  # model
        self.user_interface = UserInterface()  # view

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            article = self.user_interface.add_user_aticle()
            self.arcticle_model.add_article(article)
        elif answer == '2':
            articles = self.arcticle_model.get_all_articles()
            self.user_interface.show_all_articles(articles)

        elif answer == '3':
            article_title = self.user_interface.get_user_article()
            try:
                article = self.arcticle_model.get_singe_article(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
                self.user_interface.show_single_article(article)

        elif answer == '4':
            article_title = self.user_interface.get_user_article()
            try:
                title = self.arcticle_model.remove_article(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
               self.user_interface.remove_single_artticle(title)
        elif answer == 'q':
            self.arcticle_model.save_data()
        else:
            self.user_interface. show_incorrect_answer_error(answer)

