"""
 * @Author: Tuffy Tian 
 * @Date: 2020/4/17 3:37 PM 
 * @Last Modified by: Tuffy Tian 
 * @Last Modified time: 2020/4/17 3:37 PM
"""

from faker import Faker
from .models import User, TodoList, Todo
from .extensions import db


fake = Faker()


def fake_user() -> None:
    user = User(
        username="tuffytian",
        email="tiantengfei@outlook.com",
        sex=0,
        password="test",
    )
    db.session.add(user)
    db.session.commit()


def fake_todo_list() -> None:
    todo_list = TodoList(
        title="Default",
        user_id=1
    )
    db.session.add(todo_list)
    db.session.commit()


def fake_todo() -> None:
    for i in range(5):
        todo = Todo(
            title=fake.text(10),
            list_id=1,
            is_complete=False
        )
        db.session.add(todo)
    db.session.commit()