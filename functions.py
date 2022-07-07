from json import load


# Функция выгрузки данных
def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return load(file)


# Возврат на главную страницу
def back_home():
    return f'<a href="/"><h3>На главную</h3></a>'


# Получение ссылки на определенную старницу навыка
def get_link(_list):
    html_link = ''
    for name in _list:
        html_link += f"<a href = '/skills/{name}'> {name.title()}</a>, "
    return html_link.rstrip(', ')
