from flask import Flask
from raven.contrib.flask import Sentry

import config
from kizuna.support import Kizuna
from .views import blueprint as views_blueprint

DEV_INFO = Kizuna.read_dev_info('./.dev-info.json')

app = Flask(__name__, static_folder=config.STATIC_DIR)

app.secret_key = config.SECRET_KEY

app.config['SENTRY_CONFIG'] = {
    'dsn': config.SENTRY_URL,
    'release': DEV_INFO.get('revision'),
    'environment': config.KIZUNA_ENV
}

sentry = Sentry(app) if config.SENTRY_URL else None

app.register_blueprint(views_blueprint)
