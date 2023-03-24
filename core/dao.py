import os
import json
import math
import hashlib
import collections
from datetime import datetime

from flask import current_app
from flask_login import login_user, logout_user, current_user, login_required
from models import db, User



class UserDAO:
    def __init__(self, model):
        self.model = model
    
    def get_user(self, user_id=None, username=None):
        """
        Get user data from database.

        `Required`
        :param int user_id:  User ID
        OR
        :param str username: Username
        """
        user = None
        if user_id:
            user = db.session.query(self.model).get(user_id)
        elif username:
            user = db.session.query(self.model).filter_by(username=username).first()
        return user

    def add_user(self, username, hashed_password):
        """
        Add user to database.

        `Required`
        :param str username:        username
        :param str hashed_password: bcrypt hashed password
        """
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user



user_dao = UserDAO(User)
