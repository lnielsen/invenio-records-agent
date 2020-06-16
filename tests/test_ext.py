# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Agent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_records_agent import InvenioRecordsAgent


def test_version():
    """Test version import."""
    from invenio_records_agent import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioRecordsAgent(app)
    assert 'invenio-records-agent' in app.extensions

    app = Flask('testapp')
    ext = InvenioRecordsAgent()
    assert 'invenio-records-agent' not in app.extensions
    ext.init_app(app)
    assert 'invenio-records-agent' in app.extensions
