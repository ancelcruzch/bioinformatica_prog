from flask import Flask, render_template

from .routes import star_alignment

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        from .routes import (
            complete_linkage,
            global_alignment,
            local_alignment,
            neighbor_joining,
            star_alignment,
            point_matrix,
            protein_alignment,
            rooted_tree,
            simple_linkage,
            watson_crick,
            weighted_linkage,
            sequences
        )

        app.register_blueprint(complete_linkage.bp)
        app.register_blueprint(global_alignment.bp)
        app.register_blueprint(local_alignment.bp)
        app.register_blueprint(neighbor_joining.bp)
        app.register_blueprint(point_matrix.bp)
        app.register_blueprint(protein_alignment.bp)
        app.register_blueprint(rooted_tree.bp)
        app.register_blueprint(simple_linkage.bp)
        app.register_blueprint(star_alignment.bp)
        app.register_blueprint(watson_crick.bp)
        app.register_blueprint(weighted_linkage.bp)
        app.register_blueprint(sequences.bp)

    return app
