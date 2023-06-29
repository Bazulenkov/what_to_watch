from opinions_app import create_app, db  # noqa

# from opinions_app.models import User, Opinion


app = create_app()

# @app.shell_context_processor
# def make_shell_context():
#     return {"db": db, "User": User, "Opinion": Opinion}
