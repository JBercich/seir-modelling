#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# from simpyl.resource import Resource


import inspect
from typing import Callable, TypeAlias, Any
from typing_extensions import Unpack

# from simpyl.resources import Resource


# InteractionInput: type = Unpack[Resource]
# InteractionFunction: type = TypeAlias[Callable[[InteractionInput], Any]]


class SystemModelCollector:
    pass


class SystemModel:
    def __init__(self):
        self.interactions = []

    def continuous(self, function):
        self.interactions.append(function)

        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        return wrapper


test = SystemModel()


@test.continuous
def test_test(arg):
    print(arg)
    return arg


test.interactions.append(test_test)


print([i.__name__ for i in test.interactions])
arg = test_test("print this")
print(arg)


class SystemRegistry:
    def __init__(self):
        self.resource_registry = Registry(Resource)
        self.interaction_registry = Registry(Callable)

    def register_resource(self, *resources: Resource):
        for resource in resources:
            self.resource_registry.register(resource)

    def register_intearction(self, *interactions: Callable):
        for interaction in interactions:
            self.interaction_registry.register(interaction)


# class SimulationCollector:
#     @staticmethod
#     def deco(env):
#         def wrapper(func):
#             env.append(func)

#             def wrapper_func(*args, **kwargs):
#                 wrapper()

#             return wrapper_func

#         return wrapper


# tl = []


# @SimulationCollector.deco(tl)
# def t():
#     print(1)


# print(tl)
# # class FunDecorator:
# #     def __init__(self):
# #         self.registry = []

# #     def __call__(self, m):
# #         "This method is called when some method is decorated"
# #         self.registry.append(m)  # Add function/method to the registry

# #         def w(my_arg):
# #             print(my_arg, m)

# #         return w

# #     def run(self):
# #         print([i.__name__ for i in self.registry])


# # run_this_method = FunDecorator()  # Create class instance to be used as decorator


# # @run_this_method
# # def method_with_custom_name(my_arg):
# #     return "The args is: " + my_arg


SystemRegistry()
# import inspect
# from typing import Callable, TypeAlias, Any
# from typing_extensions import Unpack

# from simpyl.resources import Resource


# InteractionInput: type = Unpack[Resource]
# InteractionFunction: type = TypeAlias[Callable[[InteractionInput], Any]]


# class SystemModelCollector:
#     pass


# class SystemModel:
#     def __init__(self):
#         self.interactions = []

#     def continuous(self, function):
#         self.interactions.append(function)

#         def wrapper(*args, **kwargs):
#             return function(*args, **kwargs)

#         return wrapper


# test = SystemModel()


# @test.continuous
# def test_test(arg):
#     print(arg)
#     return arg


# test.interactions.append(test_test)


# print([i.__name__ for i in test.interactions])
# arg = test_test("print this")
# print(arg)


# # class SimulationCollector:
# #     @staticmethod
# #     def deco(env):
# #         def wrapper(func):
# #             env.append(func)

# #             def wrapper_func(*args, **kwargs):
# #                 wrapper()

# #             return wrapper_func

# #         return wrapper


# # tl = []


# # @SimulationCollector.deco(tl)
# # def t():
# #     print(1)


# # print(tl)
# # # class FunDecorator:
# # #     def __init__(self):
# # #         self.registry = []

# # #     def __call__(self, m):
# # #         "This method is called when some method is decorated"
# # #         self.registry.append(m)  # Add function/method to the registry

# # #         def w(my_arg):
# # #             print(my_arg, m)

# # #         return w

# # #     def run(self):
# # #         print([i.__name__ for i in self.registry])


# # # run_this_method = FunDecorator()  # Create class instance to be used as decorator


# # # @run_this_method
# # # def method_with_custom_name(my_arg):
# # #     return "The args is: " + my_arg
