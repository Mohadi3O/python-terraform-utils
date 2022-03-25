# internal
from terraform_model.utils.errors import TerraformTypeError


def is_instance(obj, cls):
    from terraform_model.internal.tftype import is_instance
    if not is_instance(obj, cls):
        raise TerraformTypeError(f'{repr(obj)} is not an instance of {cls}')


def same_type(*args):
    from terraform_model.internal.tftype import tftype
    if len(args) <= 1:
        return
    tftype_0 = tftype(args[0])
    for t in args:
        if tftype(t) is not tftype_0:
            raise TerraformTypeError(f'Not all items are the same type: {args}')


def same_type_deep(*args):
    from terraform_model.internal.tftype import tftype
    if len(args) <= 1:
        return
    tftype_0 = tftype(args[0], deep=True)
    for t in args:
        if tftype(t, deep=True) != tftype_0:
            raise TerraformTypeError(f'Not all items are the same deep type: {args}')


def same_element_type(*collections):
    if len(collections) > 1:
        element_types = [c.element_type() for c in collections]
        same_type(*element_types)


def same_element_type_deep(*collections):
    if len(collections) > 1:
        element_types = [c.element_type(deep=True) for c in collections]
        same_type_deep(*element_types)


def element_type_is(collection, element_type):
    is_(collection.element_type(), element_type)


def element_type_is_instance(collection, cls):
    is_instance(collection.element_type(), cls)


def is_(this, that):
    if this is not that:
        raise TerraformTypeError(f'{repr(this)} is not {repr(that)}')


def all_is(*objects):
    if len(objects) > 1:
        for obj in objects:
            is_(obj, objects[0])


def all_is_instance(cls, *objects):
    _ = [is_instance(obj, cls) for obj in objects]


def is_number(obj):
    from terraform_model.types.primitives import TfNumber
    if not isinstance(obj, TfNumber):
        raise TerraformTypeError(f'Expected a number. Got {repr(obj)}')


def is_bool(obj):
    from terraform_model.types.primitives import TfBool
    if not isinstance(obj, TfBool):
        raise TerraformTypeError(f'Expected a bool. Got {repr(obj)}')
