from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    
    # Import routes
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app
