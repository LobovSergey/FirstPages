# Функция линков. Подробнее в functions.py
from functions import get_link


class Candidates:

    def __init__(self, file):
        self.file = file

    # Решил немного отформатировать текст
    # Функция вывода всех кандидатов
    def get_all(self):
        html_all = ''
        for i in self.file:
            list_skills = i["skills"].lower().split(', ')
            html_all += f'<a href="/candidate/{i["pk"]}"><h3>{i["name"]}</h3></a>' \
                        f'<p><strong>Position</strong> - {i["position"]}</p>' \
                        f'<p><strong>Skills</strong>:  {get_link(list_skills)}</p><hr />'
        return html_all

    # Функция вывода кандидатов по порядковому номеру
    def get_by_pk(self, pk):
        for i in self.file:
            list_skills = i["skills"].lower().split(', ')
            if i["pk"] == pk:
                return f'<p><img src= {i["picture"]}></p>' \
                       f'<p><strong><h3>{i["name"]}</h3></strong></p>' \
                       f'<p><strong>Position</strong> - {i["position"]}</p>' \
                       f'<p><strong>Skills</strong>:  {get_link(list_skills)}</p><hr />'
        return f'<h1>Incorrect pk</h1>'

    # Функция вывода кандидатов по навыку
    def get_by_skill(self, skill):
        html_skill = ''
        for i in self.file:
            list_skills = i["skills"].lower().split(', ')
            if skill in list_skills:
                html_skill += f'<a href="/candidate/{i["pk"]}"><h3>{i["name"]}</h3></a>' \
                              f'<p><strong>Position</strong> - {i["position"]}</p>' \
                              f'<p><strong>Skills</strong>:  {get_link(list_skills)}</p><hr />'
        if len(html_skill) != 0:
            return html_skill
        return f'<h1>Incorrect skill</h1>'
