# std
import argparse


def root(args):
    if args.subcommand == 'version':
        from terraform_model.cli.subcommands.version import version
        version()
    elif args.subcommand == 'compile':
        from terraform_model.cli.subcommands.compile import compile_terraform_model
        compile_terraform_model(args)
    elif args.subcommand == 'doc':
        from terraform_model.cli.subcommands.doc import doc_terraform_model
        doc_terraform_model(args)
    elif args.subcommand in ['terraform', 'tf', 't']:
        from terraform_model.cli.subcommands.terraform import terraform
        terraform(args)
    elif args.subcommand == 'providers':
        from terraform_model.cli.subcommands.providers import get_providers
        get_providers(args)


# root
parser_root = argparse.ArgumentParser('terraform-model')
parser_root.add_argument('-v', action='count', default=0, help='Set log level.')
parser_root.add_argument('--info', action='store_true', help='Set log level to info.')
parser_root.add_argument('--verbose', action='store_true', help='Set log level to verbose.')
parser_root.add_argument('--debug', action='store_true', help='Set log level to debug.')
parser_root.add_argument('--trace', action='store_true', help='Set log level to trace.')
parser_root.add_argument('--silly', action='store_true', help='Set log level to silly.')
parser_root.set_defaults(func=root)

subparsers = parser_root.add_subparsers(dest='subcommand')
subparsers.required = True
subparsers.dest = 'subcommand'

# version
parser_version = subparsers.add_parser('version')

# compile
parser_compile = subparsers.add_parser('compile')
parser_compile.add_argument('--filepath', '-f', default='main.py')
parser_compile.add_argument('--init', action='store_true')
parser_compile.add_argument('--validate', action='store_true')

# doc
parser_doc = subparsers.add_parser('doc')
parser_doc.add_argument('--filepath', '-f', default='main.py')
parser_doc.add_argument('--output', '-o', default='DOC.md')
parser_doc.add_argument('--init', action='store_true')
parser_doc.add_argument('--validate', action='store_true')
parser_doc.add_argument('--graph', action='store_true')
parser_doc.add_argument('--graph-output', default='graph.svg')

# terraform
parser_terraform = subparsers.add_parser('terraform', aliases=['tf', 't'])
parser_terraform.add_argument('args', nargs='+')

# providers
parser_providers = subparsers.add_parser('providers')
