from flask import Flask, request, session
from flask_babel import Babel

import config
from repository.json_repository import JsonEnvelopeRepository
from service.envelope_service import EnvelopeService
from web.routes import create_routes


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY

    def get_locale():
        lang = request.args.get("lang")
        if lang in ("en", "es"):
            session["lang"] = lang
        if "lang" in session:
            return session["lang"]
        return request.accept_languages.best_match(["en", "es"])

    Babel(app, default_locale="en", locale_selector=get_locale)

    repository = JsonEnvelopeRepository(config.ENVELOPES_PATH)
    service = EnvelopeService(repository)

    app.register_blueprint(create_routes(service))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
