from random import randrange

from flask import abort, render_template, flash, redirect, url_for
from flask_login import login_required

from opinions_app import app, db
from opinions_app.forms import OpinionForm
from opinions_app.models import Opinion


def random_opinion():
    quantity = Opinion.query.count()
    if quantity:
        offset_value = randrange(quantity)
        opinion = Opinion.query.offset(offset_value).first()
        return opinion


@app.route("/")
def index_view():
    opinion = random_opinion()
    if opinion is not None:
        return render_template("opinion.html", opinion=opinion)
    abort(404)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first() is not None:
            # вызвать функцию flash и передать соответствующее сообщение
            flash("Такое мнение уже было оставлено ранее!")
            # и вернуть пользователя на страницу «Добавить новое мнение»
            return render_template("add_opinion.html", form=form)
        opinion = Opinion(
            title=form.title.data, text=form.text.data, source=form.source.data
        )
        # Затем добавить его в сессию работы с базой данных
        db.session.add(opinion)
        # И зафиксировать изменения
        db.session.commit()
        # Затем перейти на страницу добавленного мнения
        return redirect(url_for("opinion_view", id=opinion.id))
    # Иначе просто отрисовать страницу с формой
    return render_template("add_opinion.html", form=form)


@app.route("/opinions/<int:id>")
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template("opinion.html", opinion=opinion)
