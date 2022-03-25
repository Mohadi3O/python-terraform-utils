# std
from json import JSONEncoder, dump as _dump, dumps as _dumps

# internal
from terraform_model.internal.deferred import deferred
from terraform_model.utils.open import Open


class TerraformJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            return deferred.tfstringify(obj)
        except NotImplementedError:
            pass

        # noinspection PyBroadException
        try:
            return JSONEncoder.default(self, obj)
        except:
            return str(obj)


def dump(obj, filepath: str):
    with Open(filepath, mode='w') as fh:
        _dump(obj, fh, cls=TerraformJSONEncoder, indent=2, sort_keys=True)


def dumps(obj):
    return _dumps(obj, cls=TerraformJSONEncoder, indent=2, sort_keys=True)
