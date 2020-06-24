# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Agent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Query interpreter API."""

from elasticsearch_dsl import Q


class QueryInterpreter:
    """Query interpreter."""

    def __init__(self, **kwargs):
        """Constructor."""
        self.params = kwargs

    def apply(self, s):
        """Perform query."""
        return s.search(Q("query_string", "q"))
