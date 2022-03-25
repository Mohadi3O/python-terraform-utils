# std
from typing import cast, Optional as Opt

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tflist, TfList, TfNumber
from terraform_model.internal import tfassert
from terraform_model.internal.tftype import NumberLike


class TfRange(TfCollectionFunction):
    element_type = TfNumber

    def __init__(self,
            start_or_max: TfNumber,
            limit: Opt[TfNumber] = None,
            step: Opt[TfNumber] = None,
    ):
        if step is not None:
            tfassert.all_is_instance(TfNumber, start_or_max, limit, step)
            super().__init__('range', start_or_max, limit, step)
        elif limit is not None:
            tfassert.all_is_instance(TfNumber, start_or_max, limit)
            super().__init__('range', start_or_max, limit)
        else:
            tfassert.all_is_instance(TfNumber, start_or_max)
            super().__init__('range', start_or_max)


def tfrange(
        start_or_max: NumberLike,
        limit: Opt[NumberLike] = None,
        step: Opt[NumberLike] = None,
) -> TfList[TfNumber]:
    start_or_max = cast(TfNumber, typify(start_or_max))
    limit = limit if limit is None else cast(TfNumber, typify(limit))
    step = step if step is None else cast(TfNumber, typify(step))
    return tflist(TfRange(start_or_max, limit, step))
