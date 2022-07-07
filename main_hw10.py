# Импорт
from flask import Flask

from class_candidates import *
from functions import load_candidates, back_home
# Сделал экземпляр класса. Подробнее в class_candidates.py
candidates = Candidates(load_candidates())

app = Flask(__name__)


# Главный роут
@app.route("/")
def main_page():
    return candidates.get_all()


# Добавил ссылки "На главную" через back_home()
@app.route("/candidate/<int:uid>")
def canditates(uid):
    return candidates.get_by_pk(uid) + back_home()


@app.route("/skills/<uid>")
def skills(uid):
    return candidates.get_by_skill(uid) + back_home()


# Порт иногда забивает. Если не работает, то поменяйте номер порта
if __name__ == '__main__':
    app.run(host='127.0.0.3', port=8000)
