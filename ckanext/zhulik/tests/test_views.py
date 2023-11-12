"""Tests for views.py."""

import pytest

import ckanext.zhulik.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "zhulik")
@pytest.mark.usefixtures("with_plugins")
def test_zhulik_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("zhulik.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, zhulik!"
