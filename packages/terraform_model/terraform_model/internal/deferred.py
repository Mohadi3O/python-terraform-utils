class Deferred:

    @property
    def TfType(self):
        from terraform_model.types.internal.tftype import TfType
        return TfType

    @property
    def TfBool(self):
        from terraform_model.types.primitives.tfbool import TfBool
        return TfBool

    @property
    def true(self):
        from terraform_model.types import true
        return true

    @property
    def false(self):
        from terraform_model.types import false
        return false

    @property
    def tfbool(self):
        from terraform_model.types.primitives.tfbool import tfbool
        return tfbool

    @property
    def TfNull(self):
        from terraform_model.types.primitives.tfnull import TfNull
        return TfNull

    @property
    def null(self):
        from terraform_model.types import null
        return null

    @property
    def tfnull(self):
        from terraform_model.types.primitives.tfnull import tfnull
        return tfnull

    @property
    def TfNumber(self):
        from terraform_model.types import TfNumber
        return TfNumber

    @property
    def tfnumber(self):
        from terraform_model.types.primitives.tfnumber import tfnumber
        return tfnumber

    @property
    def TfString(self):
        from terraform_model.types import TfString
        return TfString

    @property
    def tfstring(self):
        from terraform_model.types.primitives.tfstring import tfstring
        return tfstring

    @property
    def TfList(self):
        from terraform_model.types import TfList
        return TfList

    @property
    def tflist(self):
        from terraform_model.types.collections.tflist import tflist
        return tflist

    @property
    def TfMap(self):
        from terraform_model.types import TfMap
        return TfMap

    @property
    def tfmap(self):
        from terraform_model.types.collections.tfmap import tfmap
        return tfmap

    @property
    def TfUnknown(self):
        from terraform_model.types.internal.tfunknown import TfUnknown
        return TfUnknown

    @property
    def tfunknown(self):
        from terraform_model.types.internal.tfunknown import tfunknown
        return tfunknown

    @property
    def TfAny(self):
        from terraform_model.types.internal.tfany import TfAny
        return TfAny

    @property
    def tfany(self):
        from terraform_model.types.internal.tfany import tfany
        return tfany

    @property
    def typify(self):
        from terraform_model.types.conversions.typify import typify
        return typify

    @property
    def tfstringify(self):
        from terraform_model.internal.tfstringify import tfstringify
        return tfstringify

    @property
    def get_type(self):
        from terraform_model.internal.tftype import tftype
        return tftype

    @property
    def get_element_type(self):
        from terraform_model.internal.tftype import get_element_tftype
        return get_element_tftype

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
    def index(self):
        from terraform_model.expressions.expressions.index import index
        return index

    @property
    def logical(self):
        from terraform_model.expressions.expressions.logical import logical
        return logical

    @property
    def unary(self):
        from terraform_model.expressions.expressions.unary import unary
        return unary

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

    @property
    def GetAttrMixin(self):
        from terraform_model.mixins import GetAttrMixin
        return GetAttrMixin

    @property
    def tfchunklist(self):
        from terraform_model.functions import tfchunklist
        return tfchunklist

    @property
    def tfconcat(self):
        from terraform_model.functions import tfconcat
        return tfconcat

    @property
    def tfcontains(self):
        from terraform_model.functions import tfcontains
        return tfcontains

    @property
    def tfdistinct(self):
        from terraform_model.functions import tfdistinct
        return tfdistinct

    @property
    def tfelement(self):
        from terraform_model.functions import tfelement
        return tfelement

    @property
    def tfindex(self):
        from terraform_model.functions import tfindex
        return tfindex

    @property
    def tfkeys(self):
        from terraform_model.functions import tfkeys
        return tfkeys

    @property
    def tflength(self):
        from terraform_model.functions import tflength
        return tflength

    @property
    def tflookup(self):
        from terraform_model.functions import tflookup
        return tflookup

    @property
    def tfmerge(self):
        from terraform_model.functions import tfmerge
        return tfmerge

    @property
    def tfreverse(self):
        from terraform_model.functions import tfreverse
        return tfreverse

    @property
    def tfsetintersection(self):
        from terraform_model.functions import tfsetintersection
        return tfsetintersection

    @property
    def tfsetsubtract(self):
        from terraform_model.functions import tfsetsubtract
        return tfsetsubtract

    @property
    def tfsetunion(self):
        from terraform_model.functions import tfsetunion
        return tfsetunion

    @property
    def tfslice(self):
        from terraform_model.functions import tfslice
        return tfslice

    @property
    def tfsort(self):
        from terraform_model.functions import tfsort
        return tfsort

    @property
    def tfvalues(self):
        from terraform_model.functions import tfvalues
        return tfvalues

    @property
    def tftype(self):
        from terraform_model.internal import tftype
        return tftype


deferred = Deferred()
