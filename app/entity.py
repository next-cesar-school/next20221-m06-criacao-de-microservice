from app.config_db import db
from sqlalchemy import ForeignKey
import app.constants as const


class ProjectUserEntity(db.Model):
    __tablename__ = 'projects_users'

    project_id = db.Column("project_id", ForeignKey(
        "projects.id"), primary_key=True)
    user_id = db.Column("user_id", ForeignKey("users.id"), primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id

    def json(self):
        return {
            'project_id': self.project_id,
            'user_id': self.user_id
        }

    def save_project_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_project_all_users(cls, id):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
        project_user = cls.query.filter_by(project_id=id).all()
        if project_user:
            return project_user
        return None

    @classmethod
    def find_project_by_user(cls, id_project, id_user):
        project_user = cls.query.filter_by(
            project_id=id_project, user_id=id_user).first()
        if project_user:
            return project_user
        return None

    def delete_project_user(self):
        db.session.delete(self)
        db.session.commit()


class ProjectEntity(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(const.CHARS_NAME))
    id_cost_center = db.Column(db.Integer, ForeignKey('cost_center.id'))
    start_date = db.Column(db.String(const.CHARS_DATE))
    end_date = db.Column(db.String(const.CHARS_DATE))
    status = db.Column(db.Enum('ongoing', 'on hold', 'finished', 'on approval'))
    flag = db.Column(db.Enum('red', 'yellow', 'green'))
    id_manager = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    user_allocated = db.relationship(
        'UsersEntity', secondary='projects_users', back_populates='allocations')

    def __init__(self, name, id_cost_center, start_date, end_date, status, flag, id_manager):
        self.name = name
        self.id_cost_center = id_cost_center
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.flag = flag
        self.id_manager = id_manager

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'id_cost_center': self.id_cost_center,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'status': self.status,
            'flag': self.flag,
            'id_manager': self.id_manager,
        }

    @classmethod
    def find_project(cls, id):
        # SELECT * FROM projects WHERE id(do db) = id(do parametro)
        project = cls.query.filter_by(id=id).first()
        if project:
            return project
        return None

    def save_project(self):
        db.session.add(self)
        db.session.commit()

    def update_project(self, name, id_cost_center, start_date, end_date, status, flag, id_manager):
        self.name = name
        self.id_cost_center = id_cost_center
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.flag = flag
        self.id_manager = id_manager

    def delete_project(self):
        db.session.delete(self)
        db.session.commit()


class UsersEntity(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(const.CHARS_NAME))
    last_name = db.Column(db.String(const.CHARS_NAME))
    birth_date = db.Column(db.String(const.CHARS_DATE))
    function = db.Column(db.String(const.CHARS_NAME))
    registration_number = db.Column(
        db.String(const.CHARS_REGISTRATION_NUMBER), unique=True)
    status = db.Column(db.Enum('active', 'inactive'))
    id_cost_center = db.Column(db.Integer, ForeignKey('cost_center.id'))
    allocations = db.relationship(
        'ProjectEntity', secondary='projects_users', back_populates='user_allocated')

    gerente = db.relationship(ProjectEntity)

    def __init__(self, first_name, last_name, birth_date, function, registration_number, status, id_cost_center):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.function = function
        self.registration_number = registration_number
        self.status = status
        self.id_cost_center = id_cost_center

    def json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'function': self.function,
            'registration_number': self.registration_number,
            'status': self.status,
            'id_cost_center': self.id_cost_center
        }

    @classmethod
    def find_user(cls, id):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None

    @classmethod
    def find_user_registration_number(cls, registration_number):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
        user_registration_number = cls.query.filter_by(registration_number=registration_number).first()

        if user_registration_number:
            return user_registration_number
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_user_registration_number(cls, registration_number):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
        user_registration_number = cls.query.filter_by(registration_number=registration_number).first()

        if user_registration_number:
            return user_registration_number
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self, first_name, last_name, birth_date, function, registration_number, status, id_cost_center):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.function = function
        self.registration_number = registration_number
        self.status = status
        self.id_cost_center = id_cost_center

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()


class CostCenterEntity(db.Model):
    __tablename__ = 'cost_center'

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(const.CHARS_NAME), unique=True)

    user = db.relationship(UsersEntity)
    project = db.relationship(ProjectEntity)

    def __init__(self, department_name):
        self.department_name = department_name

    def json(self):
        return {
            'id': self.id,
            'department_name': self.department_name
        }

    @classmethod
    def find_center(cls, id):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
        center = cls.query.filter_by(id=id).first()
        if center:
            return center
        return None

    @classmethod
    def find_center_department(cls, department_name):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
        center_department = cls.query.filter_by(department_name=department_name).first()

        if center_department:
            return center_department
        return None

    def save_center(self):
        db.session.add(self)
        db.session.commit()

    def update_center(self, department_name):
        self.department_name = department_name

    def delete_center(self):
        db.session.delete(self)
        db.session.commit()
