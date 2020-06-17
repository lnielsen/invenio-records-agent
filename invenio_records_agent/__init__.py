# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Agent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""High-level API for wokring with records, files, pids and search."""

from .ext import InvenioRecordsAgent
from .manager import RecordManager, RecordManagerConfig, RecordManagerFactory
from .version import __version__

__all__ = (
    '__version__',
    'InvenioRecordsAgent',
    'RecordManager',
    'RecordManagerConfig',
    'RecordManagerFactory',
)
