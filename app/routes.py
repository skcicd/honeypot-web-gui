from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title='Honeypot Dashboard')

@bp.route('/health')
def health():
    return {'status': 'ok', 'message': 'Honeypot Web GUI is running'}, 200
