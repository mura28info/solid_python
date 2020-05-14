import enum
import abc

"""
Dependency Inversion Principle

Dependency should be on abstractions not concretions A. High-level modules
should not depend upon low-level modules. Both should depend upon abstractions.


Abstractions should not depend on details. Details should depend upon
abstractions.

There comes a point in software development where our app will be largely
composed of modules.  When this happens, we have to clear things up by using
dependency injection.  High-level components depending on low-level components
to function.
"""


class Relationship(enum.Enum):
    PARENT = 0
    CHILD = 1
    SIBLINGS = 2

class Person(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class IRelationBrowser(abc.ABC):
    def find_all_child_of_parent(self, parent: str) -> list:
        pass


# This is our low-level module
class RelationShips(object):
    def __init__(self):
        self.__relation = list()

    def add_parent_and_child(self, parent: Person, child: Person):
        self.__relation.append((parent, Relationship.PARENT, child))
        self.__relation.append((child, Relationship.CHILD, parent))

    # if above relation list needs to be accessed outside, simply by making it to public.
    # but we should avoid accessing low level modules, lets add abstraction to do research on relationships

# Dependency Inversion, it depends on the abstraction
class RelationShipsInversion(IRelationBrowser):
    def __init__(self):
        self.__relation = list()

    def add_parent_and_child(self, parent: Person, child: Person):
        self.__relation.append((parent, Relationship.PARENT, child))
        self.__relation.append((child, Relationship.CHILD, parent))

    def find_all_child_of_parent(self, parent: str) -> list:
        for relation in self.__relation:
            if parent == relation[0].name:
                yield relation[2]

# This query module to research on the relationship
class Research(object):
    def __init__(self, name: str, find_relation: IRelationBrowser):
        self.find_relation = find_relation
        for c in find_relation.find_all_child_of_parent(name):
            print(c.name)

# Main method
if __name__ == '__main__':
    parent = Person("Murali", 32)
    child1 = Person("Rohan", 5)
    child2 = Person("Rohit", 5)

    rel_inver = RelationShipsInversion()
    rel_inver.add_parent_and_child(parent, child1)
    rel_inver.add_parent_and_child(parent, child2)

    r = Research("Murali", rel_inver)