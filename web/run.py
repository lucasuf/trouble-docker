from project.app import app
import project.views
import project.models

from project.incidentes.blueprint import incidentes
app.register_blueprint(incidentes, url_prefix='/incidentes')

if __name__ == '__main__':
    app.run()
