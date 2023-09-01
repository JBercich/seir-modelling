# #!/usr/bin/env python3
# # -*- coding:utf-8 -*-

# import pytest
# from uuid import UUID

# from simpyl.resources import Resource, Variable, Element

# @pytest.mark.skip("implementation changes")
# class TestResource:
#     class MockResource(Resource):
#         pass

#     @pytest.fixture
#     def mock_resource(cls):
#         return cls.MockResource()

#     def test_cannot_init_abstract_class(self, abstract_init_error_message):
#         with pytest.raises(TypeError) as exc:
#             Resource()
#         assert str(exc.value) == abstract_init_error_message

#     def test__init__(self):
#         assert "_uuid" in self.MockResource().__dir__()
#         assert isinstance(self.MockResource()._uuid, UUID)

#     def test__repr__(self, mock_resource):
#         assert mock_resource.__repr__() == f"MockResource:{mock_resource._uuid}"

#     def test__hash__(self, mock_resource):
#         assert hash(mock_resource) == hash(mock_resource._uuid)

#     def test__eq__(self, mock_resource):
#         assert mock_resource._uuid == mock_resource._uuid
#         assert mock_resource == mock_resource
#         assert mock_resource._uuid != self.MockResource()._uuid
#         assert mock_resource != self.MockResource()


# class TestVariable:
#     @pytest.fixture
#     def int_variable(cls):
#         return Variable("intVar", 1)

#     @pytest.fixture
#     def str_variable(cls):
#         return Variable("strVar", "str")

#     def test__init__(self):
#         variable: Variable = Variable("intVar", 1)
#         assert variable is not None
#         assert variable._uuid is not None
#         assert variable._name == "intVar"
#         assert variable._value == 1
#         assert variable._dtype == int

#     def test__eq__(self, int_variable, str_variable):
#         assert int_variable != str_variable
#         assert int_variable == int_variable
#         assert str_variable == str_variable
#         assert int_variable == Variable("intVar", 1)
#         assert str_variable == Variable("strVar", "str")
#         assert int_variable != Variable("intVarDiff", 1)
#         assert str_variable != Variable("strVarDiff", "str")
#         assert int_variable != Variable("intVar", 2)
#         assert str_variable != Variable("strVar", "strDiff")

#     def test__lt__(self, int_variable, str_variable):
#         assert int_variable < 2
#         assert int_variable < Variable("intVar", 2)
#         assert int_variable < Variable("intVarDiff", 2)
#         assert str_variable < "stra"
#         assert str_variable < Variable("strVar", "stra")
#         assert str_variable < Variable("strVarDiff", "stra")
#         with pytest.raises(TypeError):
#             int_variable < str_variable

#     def test__add__(self, int_variable, str_variable):
#         pass

#     def test__sub__(self):
#         pass

#     def test__mul__(self):
#         pass

#     def test__div__(self):
#         pass


# class TestElement:
#     class MockElement(Element):
#         field: int = 1

#     @pytest.fixture
#     def mock_element(cls):
#         return cls.MockElement()

#     def test_cannot_init_abstract_class(self, abstract_init_error_message):
#         with pytest.raises(TypeError) as exc:
#             Element()
#         assert str(exc.value) == abstract_init_error_message

#     def test_dataclass_fields(self, mock_element):
#         assert "field" in dir(mock_element)
#         assert mock_element.field == 1
