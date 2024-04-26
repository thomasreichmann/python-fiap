import os
import sys

import sqlalchemy
from databases import Database
from sanic import Sanic, response
from sanic.views import HTTPMethodView
from sanic_jinja2 import SanicJinja2
from sanic_jwt import Initialize, protected
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///fallback.db")
engine = create_async_engine(DATABASE_URL, echo=True)
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String),
)

app = Sanic("AsyncApp")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-secret-key")
jinja = SanicJinja2(app)


# Authentication function
async def authenticate(request, *args, **kwargs):
    username = request.json.get("username")
    password = request.json.get("password")
    query = users.select().where(users.c.email == username)
    user = await database.fetch_one(query)
    if user and user['password'] == password:
        return user
    return None


Initialize(app, authenticate=authenticate, secret=JWT_SECRET_KEY, url_prefix="/auth")


async def create_tables():
    engine = create_async_engine(str(DATABASE_URL), echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


@app.listener('before_server_start')
async def setup_database(app, loop):
    if 'create_db' in sys.argv:
        print("Creating database tables...")
        await create_tables()
        print("Database tables created successfully")
    await database.connect()


@app.listener('after_server_stop')
async def close_database(app, loop):
    await database.disconnect()


class UserView(HTTPMethodView):
    @protected()
    async def get(self, request, user_id):
        query = users.select().where(users.c.id == user_id)
        result = await database.fetch_one(query)
        return response.json(dict(result))

    @protected()
    async def post(self, request):
        data = request.json
        query = users.insert().values(**data)
        last_record_id = await database.execute(query)
        return response.json({"user_id": last_record_id})

    @protected()
    async def put(self, request, user_id):
        data = request.json
        query = users.update().where(users.c.id == user_id).values(**data)
        await database.execute(query)
        return response.json({"success": True})

    @protected()
    async def delete(self, request, user_id):
        query = users.delete().where(users.c.id == user_id)
        await database.execute(query)
        return response.json({"success": True})


app.add_route(UserView.as_view(), '/users/<user_id:int>')

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=8001, debug=True)
