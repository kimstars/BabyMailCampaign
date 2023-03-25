import os
import sys
import json
import shutil
from datetime import datetime

from flask import current_app, Blueprint, flash, redirect, render_template, request, url_for, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required

from models import User,bcrypt,db

from core.dao import user_dao

from users.forms import RegistrationForm, LoginForm

# Blueprint
mailcamp = Blueprint('mailcamp', __name__)


@mailcamp.route("/")
def home():
	"""Home page"""
	return render_template("home.html")

@mailcamp.route("/login")
def login():
	"""Login page"""
	return render_template("login.html")

@mailcamp.route("/mailcamplist")
def mailcamplist():
    
    
OUTPUT_DIR = os.path.abspath("/output")



