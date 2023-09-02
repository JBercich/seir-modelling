#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
import pytest

from simpyl.model.resources.resource import Resource


@pytest.mark.skip("NotImplemented")
class TestResource:
    class MockResource(Resource):
        def __init__(self, alias: str):
            self._alias: str = alias

    class MockAbstractResource(Resource, abc.ABC):
        pass

    def test_superclass_cannot_initialise(self):
        pass

    def test_abstract_subclass_cannot_initialise(self):
        pass

    def test_subclass_can_initialise(self):
        pass

    def test_subclass_get_alias_attribute(self):
        pass

    def test_subclass_get_alias(self):
        pass

    def test_subclass_set_alias(self):
        pass

    def test_subclass_set_alias_unsupported_types(self):
        pass

    def test_subclass_alias_default(self):
        pass

    def test_subclass_is_default_alias(self):
        pass

    def test_generic_equality_by_uuid(self):
        pass

    def test_generic_equality_by_alias(self):
        pass

    def test_generic_equality_unsupported_types(self):
        pass

    def test_generic_repr_format_alias(self):
        pass
