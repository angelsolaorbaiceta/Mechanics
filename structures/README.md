# structures

The _structures_ package defines the modeling and resolution of truss structures.

![](../img/truss_structure.svg "Truss structure")

Once resolved, the solution generation diagram looks like the following:

![](../img/plane_truss_result.svg)

The _structures_ package is split into sub-packages.

## model

The _model_ package defines the model classes that represent a truss structure:

### `Node`

This class represents a node in the structure.
A node is the point where one or more bars meet.

A `Node` can be instantiated using an id an a position:


```python
from geom2d import Point
from structures.model.node import StrNode

node = StrNode(1, Point(10, 35))
```

You can optionally pass a list of loads:

```python
from geom2d import Point, Vector
from structures.model.node import StrNode

loads = [Vector(0, -50), Vector(100, 0)]
node = StrNode(1, Point(10, 35), loads)
```

and add external constraints to the X and Y displacements:

```python
from geom2d import Point, Vector
from structures.model.node import StrNode

node = StrNode(
    _id=1, 
    position=Point(10, 35), 
    loads=[Vector(0, -50), Vector(100, 0)],
    dx_constrained=True,
    dy_constrained=True
)
```

### `Bar`

This class represents a resistant element whose geometry is a straight line segment.

A `Bar` is created with an id, two end nodes, a cross section value and a value for the Young modulus:

```python
from geom2d import Point
from structures.model.node import StrNode
from structures.model.bar import StrBar

node_one = StrNode(1, Point(10, 35))
node_two = StrNode(2, Point(150, 400))
bar = StrBar(
    _id=1, 
    start_node=node_one, 
    end_node=node_two,
    cross_section=25,
    young_mod=20000000
)
```

### `Structure`

A truss `Structure` is a group of linear resistant elements (bars) that joined together are meant to withstand the application of external loads.

A `Structure` is instantiated passing it the sequence of nodes and bars:

```python
nodes = [...]
bars = [...]
structure = Structure(nodes, bars)
```

This class defines a method to solve the structure and obtain the node displacements and reaction forces, as well as the stresses on each of the bars.

```python
solution = structure.solve_structure()
```

## solution

The _solution_ package define the model classes representing the structural elements with their solution values.
This package contains the same elements as _model_ (node, bar and structure), but with their solution values included: `StrNodeSolution`, `StrBarSolution` and `StructureSolution`.

## parse

TODO

## generation

TODO

## out

TODO

