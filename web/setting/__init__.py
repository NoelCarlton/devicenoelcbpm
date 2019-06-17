from flask import Blueprint
from config import TEMPLATES_DIR, STATICFILES_DIR

setting = Blueprint('setting', __name__, template_folder= TEMPLATES_DIR, static_folder= STATICFILES_DIR)

from web.setting import views