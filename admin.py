from wtforms.fields.core import StringField
from models import (
    Usuário, 
    Tarefa,
    Perfil
)
from app import db
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash
# from flask_login import current_user


class UserView(ModelView):
    # form_excluded_columns = ('tarefa')
    column_editable_list = ('nome', 'email', 'tarefa')
    form_edit_rules = {'nome', 'email', 'tarefa', 'perfil'}
    column_searchable_list = ['email']
    edit_modal = True
    
    form_extra_fields = {
        "senha": PasswordField("Senha",validators=[
            DataRequired("O campo é obrigatório")
        ]),
    }

    inline_models = [Perfil]

    column_filters = ['email', 'perfil']
    # column_exclude_list = ('senha', 'tarefa')
    column_list =["nome", "email", "perfil"]

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.senha = generate_password_hash(form.senha.data)
        # return super().on_model_change(form, model, is_created)

    
    # def is_accessible(self):
    #     return current_user.is_authenticated("True")
    #     # return super().is_accessible()


def init_app(admin):
    admin.add_view(UserView(Usuário, db.session))
    admin.add_view(ModelView(Tarefa, db.session))