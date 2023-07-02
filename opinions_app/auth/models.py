from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from opinions_app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    avatar = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # 0:35:16
    # def get_reset_password_token(self, expires_in=600):
    #     return jwt.encode(
    #         {"reset_password": self.id,
    #          "exp":}
    #     )


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
