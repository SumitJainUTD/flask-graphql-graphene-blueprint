import os
from company import company_app
from company.extenstions import db
from dotenv import load_dotenv, find_dotenv
from flask_graphql import GraphQLView
from company.schema import schema

load_dotenv(find_dotenv())
company_app = company_app.create_app()

port = os.environ.get('FLASK_RUN_PORT')


@company_app.before_first_request
def create_tables():
    db.create_all()


company_app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)

# print(schema)

company_app.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=schema, graphiql=True
))

if __name__ == '__main__':
    company_app.run(host='0.0.0.0', port=port)
