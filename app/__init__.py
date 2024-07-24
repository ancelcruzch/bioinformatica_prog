from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        from .routes import global_alignment, local_alignment, protein_alignment

        app.register_blueprint(global_alignment.bp)
        app.register_blueprint(local_alignment.bp)
        app.register_blueprint(protein_alignment.bp)

        return app
