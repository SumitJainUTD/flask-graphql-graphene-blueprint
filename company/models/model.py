from company.extenstions import db
from datetime import datetime


class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(20))
    employee_id = db.Column(db.String, db.ForeignKey("employees.id"))
    date_created = db.Column(db.DateTime, default=datetime.utcnow())


class Skill(db.Model):
    __tablename__ = 'skills'

    id = db.Column(db.String, primary_key=True)
    skill_name = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, default=datetime.utcnow())


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80))
    industry = db.Column(db.String(80))
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    employee = db.relationship("Employee")


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    project = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    skills = db.relationship("Skill", secondary="employee_skills")
    company_id = db.Column(db.String, db.ForeignKey("companies.id"))


class EmployeeSkills(db.Model):
    __tablename__ = 'employee_skills'
    id = db.Column(db.String, primary_key=True)
    employee_id = db.Column(db.String, db.ForeignKey('employees.id'))
    skill_id = db.Column(db.String, db.ForeignKey('skills.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow())


