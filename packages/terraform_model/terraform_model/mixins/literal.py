class LiteralMixin:

    # must return something json-serializable
    def literal(self):
        if hasattr(self, 'data'):
            return self.data
        raise NotImplementedError
