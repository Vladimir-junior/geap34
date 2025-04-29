import json
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from models import FormData

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            inputs = request.form.to_dict()
            area = request.form.get('area')
            if area:
                try:
                    area = json.loads(area)
                except json.JSONDecodeError:
                    area = None
            new_entry = FormData(data=inputs, area=area)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('view_data'))
        return render_template('index.html')

    @app.route('/view')
    def view_data():
        entries = FormData.query.all()
        return render_template('view.html', entries=entries)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)