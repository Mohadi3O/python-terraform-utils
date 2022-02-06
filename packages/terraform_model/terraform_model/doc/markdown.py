# std
from typing import Iterable, Union

# internal
from terraform_model.utils.open import Open


class Markdown:

    def __init__(self, name: str, level: int = 1):
        self._name = name
        self._level = level
        self._content: list[str] = []
        self._sections: list[Markdown] = []

    def section(self, name: str):
        m = Markdown(name, level=(self._level + 1))
        self._sections.append(m)
        return m

    def write(self, string: str):
        self._content.append(string)

    def write_line(self, string: str):
        self.write(f'{string}\n')

    def newline(self):
        self.write('\n')

    def table(self, data: dict):
        self.newline()
        columns: list = data['columns']
        self._write_row(map(self.b, columns))
        self._write_row(['---'] * len(columns))
        for row in data['rows']:
            self._write_row(self._format_row_items(columns, row))
        self.newline()

    def img(self, text: str, link: str):
        self.write_line(f'![{text}]({link})')

    def build(self) -> str:
        sections = [s.build() for s in self._sections]
        content = ''.join([self._build()] + sections)
        return content

    def to_file(self, filepath: str):
        with Open(filepath, mode='w') as fh:
            fh.write(self.build())

    def _write_row(self, items: Iterable):
        self.write_line(' | '.join(map(str, items)))

    def _build(self) -> str:
        header_prefix = '' if self._level == 1 else '\n\n'
        header_suffix = '\n\n'
        header = f'{header_prefix}{"#" * self._level} {self._name}{header_suffix}'
        content = ''.join([header] + self._content)
        return content

    @staticmethod
    def b(string: any) -> str:
        return f'**{string}**'

    @staticmethod
    def i(string: any) -> str:
        return f'*{string}*'

    @staticmethod
    def c(string: any) -> str:
        return f'`{string}`'

    @staticmethod
    def _format_row_items(columns: list, row: Union[dict, list]) -> list:
        if isinstance(row, dict):
            items = [row.get(c) for c in columns]
        else:
            items = [x for x in row]
        return items
