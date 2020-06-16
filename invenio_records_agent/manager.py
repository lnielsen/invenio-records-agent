# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Agent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Agent API."""

from flask_principal import Permission
from invenio_pidstore.resolver import Resolver
from invenio_records.api import Record

from .errors import PermissionDeniedError
from .state import RecordState


class RecordManagerConfig:
    """Manager configuration."""

    record_cls = Record
    resolver_cls = Resolver
    resolver_pid_type = 'recid'
    resolver_obj_type = 'rec'
    permission_policy_cls = ''
    record_state_cls = RecordState

    # pid = 'recidv2'
    # pids = ['doi', ]
    # Class dependency injection
    # indexer_class = None
    # search_class = None
    # query_interpreter_class = None
    # state_class = None
    # draft_class = None
    # result_class = None
    # action_classes = {
    #     'publish': ...
    # }


class RecordManagerFactory:
    """Factory for creating object instances and classes."""

    def __init__(self, config):
        self._config = config

    def resolver(self):
        """Factory for creating a resolver class."""
        return self._config.resolver_cls(
            pid_type=self._config.resolver_pid_type,
            getter=self._config.record_cls.get_record
        )

    def permission(self, action_name, **kwargs):
        """Factory for creating permissions from a permission policy."""
        if self._config.permission_policy_cls:
            return self._config.permission_policy_cls(action_name, **kwargs)
        else:
            return Permission()

    def item_state(self, **kwargs):
        """Create a new item state."""
        return self._config.record_state_cls(**kwargs)


class RecordManager:
    """Record manager interface."""

    factory = RecordManagerFactory(RecordManagerConfig)

    #
    # Permissions checking
    #
    @classmethod
    def require_permission(cls, identity, action_name, **kwargs):
        """Require a specific permission from the permission policy."""
        if not cls.factory.permission(action_name, **kwargs).allows(identity):
            raise PermissionDeniedError(action_name)


    #
    # Persistent identifier resolution
    #
    @classmethod
    def resolve(cls, id_):
        """Resolve a persistent identifier to a record."""
        return cls.factory.resolver().resolve(id_)


    #
    # High-level API
    #
    @classmethod
    def get(cls, id_, identity):
        """Retrieve a record."""
        pid, record = cls.resolve(id_)
        cls.require_permission(identity, 'read', record=record)
        # Todo: how do we deal with tombstone pages
        return cls.factory.item_state(pid=pid, record=record)
