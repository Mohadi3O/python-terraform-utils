# std
import os
from subprocess import call, check_output, Popen, PIPE
from typing import Optional

# internal
from .logger import log
from .errors import TerraformException

TERRAFORM = 'terraform'


# def _run(args: list[str], **kwargs):
#     return_code = call(args=args, **kwargs)
#     if return_code > 0:
#         raise TerraformException(f'Terraform exited with non-zero return code {return_code}')
#     return return_code


# def _capture(args: list[str], **kwargs):
#     return check_output(args=args, **kwargs)


def _popen(
        args: list[str],
        capture: bool = False,
        stdin: Optional[str] = None,
        **kwargs,
):
    if capture:
        kwargs['stdout'] = PIPE
    if stdin:
        kwargs['stdin'] = PIPE
    with Popen(args=args, **kwargs) as p:
        _output = None
        if stdin and capture:
            # noinspection PyTypeChecker
            _output, errs = p.communicate(bytes(stdin, 'utf-8'))
            if errs:
                raise TerraformException(errs)
            _output = str(_output, 'utf-8')
        elif stdin:
            # noinspection PyTypeChecker
            _, errs = p.communicate(bytes(stdin, 'utf-8'))
            if errs:
                raise TerraformException(errs)
            _output = p.returncode
        elif capture:
            _output = p.stdout.read()
        else:
            _output = p.returncode
        return _output


def run_terraform(*args: str, capture: bool = False, stdin: Optional[str] = None, **kwargs):
    _args = [TERRAFORM] + list(args)
    log.silly(' '.join(_args))
    if 'env' in kwargs:
        kwargs['env'] = {**os.environ, **kwargs['env']}
    return _popen(_args, capture=capture, stdin=stdin, **kwargs)
    # if capture:
    #     return _capture(_args, **kwargs)
    # else:
    #     return _run(_args, **kwargs)
