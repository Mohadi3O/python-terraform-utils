# std
from subprocess import check_output, CalledProcessError, Popen, PIPE
from typing import Optional as Opt


def is_installed() -> bool:
    try:
        version()
        return True
    except CalledProcessError:
        return False


def version():
    run(['dot', '-V'])


def run(args: list[str], stdin: Opt[bytes] = None):
    if stdin:
        p = Popen(args, stdin=PIPE)
        p.communicate(input=stdin)
    else:
        check_output(args)
