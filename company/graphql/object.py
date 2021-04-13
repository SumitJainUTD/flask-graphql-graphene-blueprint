import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from ..models.model import Profile as ProfileModel, Skill as TagModel, Company as CompanyModel, \
    Employee as EmployeeModel, EmployeeSkills as EmployeeSkillsModel, \
    EmployeeSkills as EmployeeSkillsModel, Skill as SkillModel


class Profile(SQLAlchemyObjectType):
    class Meta:
        model = ProfileModel
        interfaces = (relay.Node,)


class Skill(SQLAlchemyObjectType):
    class Meta:
        model = TagModel
        exclude_fields = ("id",)
        interfaces = (relay.Node,)


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        exclude_fields = ("id",)
        # interfaces = (relay.Node,)

    profile = graphene.List(Profile)
    skills = graphene.List(Skill)

    def resolve_profile(self, info):
        query = Profile.get_query(info=info)
        print(query)
        query = query.filter(self.id == ProfileModel.employee_id)
        print(query.all())
        return query.all()

    def resolve_skills(self, info):
        query = Skill.get_query(info=info)
        query = query.filter(self.id == EmployeeSkillsModel.employee_id)
        query = query.filter(EmployeeSkillsModel.skill_id == SkillModel.id)
        return query.all()


class Company(SQLAlchemyObjectType):
    class Meta:
        model = CompanyModel
        exclude_fields = ("id",)
        interfaces = (relay.Node,)

    employees = graphene.List(Employee)

    def resolve_employees(self, info):
        query = Employee.get_query(info=info)
        query = query.filter(EmployeeModel.company_id == self.id)
        return query.all()
