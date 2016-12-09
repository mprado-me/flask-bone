#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g

from src.blueprints.components.lightly_route_dependent.navbar.r import navbar_R

home_blueprint = Blueprint("home", __name__, static_folder="static", template_folder="templates")


@home_blueprint.route("/")
def index():
    g.active_navbar_item_id = navbar_R.id.home
    return render_template("home/home.html")
