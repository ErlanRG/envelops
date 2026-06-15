from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_babel import _

from service.envelope_service import EnvelopeService


def create_routes(service: EnvelopeService) -> Blueprint:
    bp = Blueprint("web", __name__)

    @bp.route("/")
    def index():
        envelopes = service.get_all()
        return render_template("index.html", envelopes=envelopes)

    @bp.route("/envelopes", methods=["POST"])
    def create():
        name = request.form.get("name", "")
        try:
            monthly_amount = float(request.form.get("monthly_amount", "0"))
        except ValueError:
            flash(_("Invalid monthly amount"), "error")
            return redirect(url_for("web.index"))

        cap_raw = request.form.get("cap", "")
        cap: float | None = None
        if cap_raw.strip():
            try:
                cap = float(cap_raw)
            except ValueError:
                flash(_("Invalid cap"), "error")
                return redirect(url_for("web.index"))

        try:
            service.create(name, monthly_amount, cap)
            flash(_("Envelope '%(name)s' created", name=name), "success")
        except ValueError as e:
            flash(str(e), "error")

        return redirect(url_for("web.index"))

    @bp.route("/envelopes/<envelope_id>/edit", methods=["POST"])
    def edit(envelope_id: str):
        name = request.form.get("name", "")
        try:
            monthly_amount = float(request.form.get("monthly_amount", "0"))
        except ValueError:
            flash(_("Invalid monthly amount"), "error")
            return redirect(url_for("web.index"))

        cap_raw = request.form.get("cap", "")
        cap: float | None = None
        if cap_raw.strip():
            try:
                cap = float(cap_raw)
            except ValueError:
                flash(_("Invalid cap"), "error")
                return redirect(url_for("web.index"))

        try:
            service.update(envelope_id, name, monthly_amount, cap)
            flash(_("Envelope '%(name)s' updated", name=name), "success")
        except ValueError as e:
            flash(str(e), "error")

        return redirect(url_for("web.index"))

    @bp.route("/envelopes/<envelope_id>/delete", methods=["POST"])
    def delete(envelope_id: str):
        try:
            service.delete(envelope_id)
            flash(_("Envelope deleted"), "success")
        except ValueError as e:
            flash(str(e), "error")

        return redirect(url_for("web.index"))

    return bp
