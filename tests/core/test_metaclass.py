#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
import pytest

from simpyl.model import BaseMetaclass


@pytest.mark.skip("NotImplemented")
class TestBaseMetaclass:
    class MockBaseMetaclass(BaseMetaclass):
        pass

    class MockAbstractBaseMetaclass(BaseMetaclass, abc.ABC):
        pass

    def test_superclass_cannot_initialise(self):
        pass

    def test_abstract_subclass_cannot_initialise(self):
        pass

    def test_subclass_can_initialise(self):
        pass

    def test_subclass_get_uuid_attribute(self):
        pass

    def test_subclass_get_uuid(self):
        pass

    def test_subclass_uuid_attribute_is_unique(self):
        pass

    def test_generic_equality_by_uuid(self):
        pass

    def test_generic_hash_by_uuid(self):
        pass

    def test_generic_repr_format(self):
        pass
