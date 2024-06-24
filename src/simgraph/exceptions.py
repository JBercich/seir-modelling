#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class GraphException(Exception):
    pass


class ResourceException(GraphException):
    pass


class InvalidEntityTypeException(ResourceException):
    def __init__(self, expected: type, returned: type):
        self.expected: type = expected
        self.returned: type = returned

    def __str__(self) -> str:
        return "Entity update returned type '%s' but expected type '%s' or '%s'" % (
            self.returned,
            self.expected,
            type(None),
        )
