from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Message
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat/<int:receiver_id>', methods=['GET','POST'])
def chat(receiver_id):
    if request.method == 'POST':
        # save message to DB
        pass
    # load messages from DB
    return render_template('chat.html', receiver_id=receiver_id)
