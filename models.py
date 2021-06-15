from sqlalchemy.orm import backref
from app import db # login_manager
from flask_login import UserMixin


# @login_manager.user_loader
# def current_user(user_id):
#     return Usuário.query.get(user_id)


class Usuário(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    senha = db.Column(db.String(255), nullable=False)
    tarefa = db.relationship('Tarefa', backref='usuario')
    perfil = db.relationship('Perfil', backref='usuario')

    def __repr__(self):
        return self.nome


class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return self.nome


class Perfil(db.Model):
    __tablename__ = 'perfis'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False, unique=True, index=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return self.cpf