# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Agent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Query interpreter API"""


class QueryInterpreter:
    """Query interpreter."""
    def __init__(**kwargs):
        self.params = kwargs

    def apply(s):
        return s.search(Q('query_string', 'q'))
