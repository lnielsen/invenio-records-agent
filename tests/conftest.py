# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Agent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

import shutil
import tempfile
from uuid import uuid4

import pytest
from flask import Flask
from flask_principal import Identity, Permission, UserNeed

from invenio_records_agent import InvenioRecordsAgent, RecordManager, \
    RecordManagerConfig, RecordManagerFactory
from invenio_records_agent.resolver import UUIDResolver


@pytest.fixture(scope='module')
def create_app(instance_path):
    """Application factory fixture."""
    def factory(**config):
        app = Flask('testapp', instance_path=instance_path)
        app.config.update(**config)
        InvenioRecordsAgent(app)
        return app
    return factory


@pytest.fixture()
def identity_simple():
    """Simple identity fixture."""
    i = Identity(1)
    i.provides.add(UserNeed(1))


@pytest.fixture()
def fake_record_db():
    """A fake record."""
    return {
        uuid4(): {'title': 'Fake record'},
    }


@pytest.fixture()
def fake_record_cls(fake_record_db):
    """Fake record class."""
    class FakeRecord(dict):
        @classmethod
        def get_record(cls, id_):
            fake_record = fake_record_db.get(id_)
            if fake_record:
                return cls(fake_record)
            else:
                raise Exception('Record not found')

    return FakeRecord


@pytest.fixture()
def fake_permission_policy_cls():
    """Fake record fixture."""
    class FakePermissionPolicy(Permission):
        def __init__(self, action_name, **kwargs):
            self.needs = set()
            self.excludes = set()

    return FakePermissionPolicy


@pytest.fixture()
def manager_config_cls(fake_record_cls, fake_permission_policy_cls):
    """Manager configuration class."""
    class TestRecordManagerConfig(RecordManagerConfig):
        record_cls = fake_record_cls
        resolver_cls = UUIDResolver
        permission_policy_cls = fake_permission_policy_cls

    return TestRecordManagerConfig


@pytest.fixture()
def manager_cls(manager_config_cls):
    """Record manager class."""
    class TestRecordManager(RecordManager):
        factory = RecordManagerFactory(manager_config_cls)

    return TestRecordManager
