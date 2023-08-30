#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pytest
from uuid import UUID

from simpyl.model.resource import Resource


class TestResource:
    class MockResource(Resource):
        pass

    @pytest.fixture
    def mock_resource(cls):
        return cls.MockResource()

    def test_cannot_init_abstract_class(self, abstract_init_error_message):
        with pytest.raises(TypeError) as exc:
            Resource()
        assert str(exc.value) == abstract_init_error_message

    def test__init__(self):
        assert "_uuid" in self.MockResource().__dir__()
        assert isinstance(self.MockResource()._uuid, UUID)

    def test__repr__(self, mock_resource):
        assert mock_resource.__repr__() == f"MockResource:{mock_resource._uuid}"

    def test__hash__(self, mock_resource):
        assert hash(mock_resource) == hash(mock_resource._uuid)

    def test__eq__(self, mock_resource):
        assert mock_resource._uuid == mock_resource._uuid
        assert mock_resource == mock_resource
        assert mock_resource._uuid != self.MockResource()._uuid
        assert mock_resource != self.MockResource()
