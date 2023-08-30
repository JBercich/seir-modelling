# #!/usr/bin/env python3
# # -*- coding:utf-8 -*-

# from abc import ABC, abstractmethod

# from simpyl.model.element import Element
# from simpyl.model.relationship import Relationship


# class SystemModel(ABC):
#     @abstractmethod
#     def __init__(self, elements: list[Element], relationships: list[Relationship]):
#         self.elements: list[Element] = elements
#         self.relationships: list[Relationship] = relationships


# class FunDecorator:
#     def __init__(self):
#         self.registry = []

#     def __call__(self, m):
#         "This method is called when some method is decorated"
#         self.registry.append(m)  # Add function/method to the registry

#         def w(my_arg):
#             print(my_arg, m)

#         return w


# run_this_method = FunDecorator()  # Create class instance to be used as decorator


# @run_this_method
# def method_with_custom_name(my_arg):
#     return "The args is: " + my_arg


# # do some magic with each decorated method:
# for m in run_this_method.registry:
#     print(m.__name__)
