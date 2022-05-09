from flask import Blueprint, jsonify, render_template, request

bp = Blueprint("error_handlers", __name__)


@bp.app_errorhandler(403)
def forbidden(_):
    if request.path.startswith("/api/"):
        return jsonify(message="Forbidden access."), 403
    else:
        return render_template("errors/403.html"), 403


@bp.app_errorhandler(404)
def page_not_found(_):
    if request.path.startswith("/api/"):
        return jsonify(message="Page Not Found."), 404
    return render_template("errors/404.html"), 404


@bp.app_errorhandler(405)
def method_not_allowed(e):
    if request.path.startswith("/api/"):
        return jsonify(message="Method not Alowed."), 405
    else:
        return render_template("errors/500.html"), 405


@bp.app_errorhandler(500)
def internal_server_error(_):
    if request.path.startswith("/api/"):
        return jsonify(message="Internal Server Error."), 500
    return render_template("errors/500.html"), 500
