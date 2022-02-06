class Deferred:
    @property
    def Bool(self):
        from terraform_model.types.atomics.bool import Bool
        return Bool

    @property
    def true(self):
        from terraform_model.types import true
        return true

    @property
    def false(self):
        from terraform_model.types import false
        return false

    @property
    def Null(self):
        from terraform_model.types.atomics.null import Null
        return Null

    @property
    def null(self):
        from terraform_model.types import null
        return null

    @property
    def Number(self):
        from terraform_model.types import Number
        return Number

    @property
    def String(self):
        from terraform_model.types import String
        return String

    @property
    def List(self):
        from terraform_model.types import List
        return List

    @property
    def Map(self):
        from terraform_model.types import Map
        return Map

    @property
    def Unknown(self):
        from terraform_model.types.unknown import Unknown
        return Unknown

    @property
    def typify(self):
        from terraform_model.types.typify import typify
        return typify

    @property
    def to_bool(self):
        from terraform_model.types.typify import to_bool
        return to_bool

    @property
    def to_null(self):
        from terraform_model.types.typify import to_null
        return to_null

    @property
    def to_number(self):
        from terraform_model.types.typify import to_number
        return to_number

    @property
    def to_string(self):
        from terraform_model.types.typify import to_string
        return to_string

    @property
    def to_list(self):
        from terraform_model.types.typify import to_list
        return to_list

    @property
    def to_map(self):
        from terraform_model.types.typify import to_map
        return to_map

    @property
    def Expression(self):
        from terraform_model.expressions.expression import Expression
        return Expression

    @property
    def GetAttr(self):
        from terraform_model.expressions.expressions.getattr import GetAttr
        return GetAttr

    @property
    def GetItem(self):
        from terraform_model.expressions.expressions.getitem import GetItem
        return GetItem

    @property
    def math(self):
        from terraform_model.expressions.expressions.math import math
        return math

    @property
    def compare(self):
        from terraform_model.expressions.expressions.compare import compare
        return compare

    @property
    def Block(self):
        from terraform_model.blocks.blocks.block import Block
        return Block

    @property
    def Data(self):
        from terraform_model.blocks.blocks.data import Data
        return Data

    @property
    def Local(self):
        from terraform_model.blocks.blocks.locals import Local
        return Local

    @property
    def Module(self):
        from terraform_model.blocks.blocks.module import Module
        return Module

    @property
    def Output(self):
        from terraform_model.blocks.blocks.output import Output
        return Output

    @property
    def Provider(self):
        from terraform_model.blocks.blocks.provider import Provider
        return Provider

    @property
    def Resource(self):
        from terraform_model.blocks.blocks.resource import Resource
        return Resource

    @property
    def Variable(self):
        from terraform_model.blocks.blocks.variable import Variable
        return Variable

    @property
    def ExpressionMixin(self):
        from terraform_model.mixins import ExpressionMixin
        return ExpressionMixin

    @property
    def LiteralMixin(self):
        from terraform_model.mixins import LiteralMixin
        return LiteralMixin


deferred = Deferred()
