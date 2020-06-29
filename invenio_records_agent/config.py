# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Agent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Configuration for Invenio-Records-Agent."""

from elasticsearch import VERSION as ES_VERSION

lt_es7 = ES_VERSION[0] < 7

PIDSTORE_RECID_FIELD = "recid"
