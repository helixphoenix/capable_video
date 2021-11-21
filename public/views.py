# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

from capable_video.video_app.extensions import login_manager
from capable_video.public.forms import LoginForm
from capable_video.user.forms import RegisterForm
from capable_video.user.models import User
from capable_video.video_app.utils import flash_errors

from capable_video.video_app.save_video import save_videos
from capable_video.video_app.upload_video import upload_videos
from capable_video.video_app.process_video import process_videos
# from capable_video.video_app.list_videos import list_all

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)


@blueprint.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        video = request.files['filename']
        temp_video = upload_videos(video)
        processed_video = process_videos(temp_video)
        saved_video = save_videos(processed_video)
        flash("Thank you for uploading the video. Please see the details")
        render_template("public/upload.html", filename=video)
        return render_template("public/upload.html", filename=video)
    else:
        return render_template("public/upload.html")


@blueprint.route("/list/", methods=["GET"])
def list():
    videos = list_all()
    return render_template(url_for("public.list"), videos=videos)
