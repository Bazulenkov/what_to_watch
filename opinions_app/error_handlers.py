from flask import render_template, jsonify

from opinions_app import app, db


class InvalidAPIUsage(Exception):
    # Если статус-код для ответа API не указан — вернётся код 400
    status_code = 400

    # Конструктор класса InvalidAPIUsage принимает на вход
    # текст сообщения и статус-код ошибки (необязательно)
    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        # Если статус-код передан в конструктор —
        # этот код вернётся в ответе
        if status_code is not None:
            self.status_code = status_code

    # Метод для сериализации переданного сообщения об ошибке
    def to_dict(self):
        return dict(message=self.message)


# Обработчик кастомного исключения для API
@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    # В качестве ответа возвращается собственный шаблон
    # и код ошибки
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    # В таких случаях можно откатить незафиксированные изменения в БД
    db.session.rollback()
    return render_template("500.html"), 500
