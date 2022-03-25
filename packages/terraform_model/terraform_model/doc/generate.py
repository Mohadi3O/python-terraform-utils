# std
from itertools import chain
from typing import Optional as Opt

# internal
from terraform_model.doc.markdown import Markdown
from terraform_model.blocks.blocks.block import Block
from terraform_model.blocks.blocks.variable import Variable
from terraform_model.blocks.blocks.output import Output
from terraform_model.blocks.blocks.provider import Provider
from terraform_model.helpers.scope import Scope


def generate_markdown(scope: Scope, module=None, md: Opt[Markdown] = None) -> Markdown:
    md = md if md else Markdown('Terraform Model')
    if module is not None and hasattr(module, '__doc__'):
        doc = 'No description.' if module.__doc__ is None else module.__doc__
        md.write_line(doc)
    _variables(md, scope)
    _outputs(md, scope)
    _providers(md, scope)
    _modules(md, scope)
    return md


def _variables(md: Markdown, scope: Scope):
    section = md.section('Input Variables')
    blocks = scope.get_items(Variable.type_name())
    if len(blocks) > 0:
        _blocks_table(section, blocks)
    else:
        section.write_line(str(None))


def _outputs(md: Markdown, scope: Scope):
    section = md.section('Output Values')
    blocks = scope.get_items(Output.type_name())
    if len(blocks) > 0:
        columns = ['name', 'type']
        rows = [dict(name=b.name, type=b.data['value'].tftype()) for b in blocks]
        section.table(dict(columns=columns, rows=rows))
    else:
        section.write_line(str(None))


def _providers(md: Markdown, scope: Scope):
    section = md.section('Providers')
    blocks = scope.get_items(Provider.type_name())
    if len(blocks) > 0:
        _blocks_table(section, blocks, 'sub_type')
    else:
        section.write_line(str(None))


def _modules(md: Markdown, scope: Scope):
    section = md.section('Nested Modules')
    if len(scope.children) == 0:
        section.write_line(str(None))
    else:
        for nested_module in scope.children:
            sub_section = section.section(nested_module.name)
            generate_markdown(nested_module, nested_module.module_or_function, sub_section)


def _blocks_table(section: Markdown, blocks: list[Block], name_attr: str = 'name'):
    columns = ['name'] + sorted(list(set(chain(*(b.data.keys() for b in blocks)))))
    rows = [dict(name=getattr(b, name_attr), **b.data) for b in blocks]
    section.table(dict(columns=columns, rows=rows))
