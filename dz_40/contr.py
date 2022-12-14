from view2 import UserInterface
from model1 import ArticleModel


class Controller:
    def __init__(self):
        self.atc_model = ArticleModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            article = self.user_interface.add_user_aticle()
            self.arcticle_model.add_article(article)
        elif answer == '2':
            articles = self.arcticle_model.get_all_articles()
            self.user_interface.show_all_articles(articles)
