# std
import os

# internal
from terraform_model.cli.subcommands.compile import import_module
from terraform_model.helpers.scope import Scope, DEFAULT_NAME
from terraform_model.doc.generate import generate_markdown
from terraform_model.cli.subcommands.terraform import default_terraform, validate
from terraform_model.doc import dot
from terraform_model.utils.errors import TerraformModelException


def doc_terraform_model(args):
    validate(args)
    module = import_module(args.filepath)
    scope = Scope.get_scope(DEFAULT_NAME)
    _doc_scope(args, module, scope)


def _doc_scope(args, module, scope):
    md = generate_markdown(scope, module)
    if args.graph:
        graph = _graph()
        if not dot.is_installed():
            raise TerraformModelException('Graph option is not available when graphviz is not installed.')
        if os.path.isfile(args.graph_output):
            os.remove(args.graph_output)
        dot.run(['dot', '-Tsvg', '-o', args.graph_output], stdin=graph)
        section = md.section('Resources')
        section.img('graph', f'./{args.graph_output}')
    md.to_file(args.output)


def _graph() -> bytes:
    tf = default_terraform()
    return tf.graph(capture=True)
