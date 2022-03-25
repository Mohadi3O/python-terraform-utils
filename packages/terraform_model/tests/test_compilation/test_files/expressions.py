"""
This is a basic Terraform model.
"""
from terraform_model.all import *

b = variable('b', true)
l = variable('l', [0, 1])
m = variable('m', {'x': 1})
world = variable('world', 'world')
x = variable('x', 1)
y = local('y', 2)

output('string-interpolation', f'Hello, {world:$}')
output('compare', x < y)
output('map-get-item', m['x'])
output('list-index', l[0])
output('logical', x == y)
output('unary', ~b)
output('math', x + y)
output('ternary', ternary(true, true, false))
