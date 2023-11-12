"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.zhulik.logic import validators


def test_zhulik_reauired_with_valid_value():
    assert validators.zhulik_required("value") == "value"


def test_zhulik_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.zhulik_required(None)
