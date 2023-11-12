"""Tests for helpers.py."""

import ckanext.zhulik.helpers as helpers


def test_zhulik_hello():
    assert helpers.zhulik_hello() == "Hello, zhulik!"
