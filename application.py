from config.config_provider import ConfigProvider
from flask import Flask, Blueprint
from flask_migrate import upgrade as _upgrade
from flask_cors import CORS
from sqlalchemy import create_engine

from domain.data_access_layer.engine import add_engine_pidguard, app_db_engine_provider
from domain.data_access_layer.db import db, migrate

from config.model_config import model_type
from basic_model_binding.messages_traffic_controller import MessagesTrafficController

from routes.associations_routes import associations_blueprint



def create_app(config=ConfigProvider):
    """Application factory, used to create application"""
    app = Flask(__name__)
    app.config.from_object(config)

    app.url_map.strict_slashes = False

    CORS(
        app,
    )

    app_db_engine_provider.set_engine(create_engine(
        config.SQLALCHEMY_DATABASE_URI,
        isolation_level='READ COMMITTED',
        pool_pre_ping=True,
    ))

    add_engine_pidguard(app_db_engine_provider.get_engine())

    register_blueprints(app)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        _upgrade()

    thread_for_processing_messages_with_photos = MessagesTrafficController(model_type=model_type)
    thread_for_processing_messages_with_photos.daemon = True
    thread_for_processing_messages_with_photos.start()

    return app


def register_blueprints(app):
    """Register all blueprints for application"""
    associations_service_blueprint = Blueprint('associations-service', __name__, url_prefix='/associations-service')
    associations_service_blueprint.register_blueprint(associations_blueprint)

    app.register_blueprint(associations_service_blueprint)