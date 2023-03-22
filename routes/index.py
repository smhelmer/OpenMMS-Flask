from flask import Blueprint, render_template as render

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
   return render('login/login.html')

@index_bp.route('/admin')
def admin():
   return render('index.html')