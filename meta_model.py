# Import necessary libraries
from typing import Optional, List, Dict, Literal
from datetime import datetime

class Author:
    """
    Represents an author of a metadata object.

    Attributes:
    - code (str): Unique code identifying the author.
    - name (str): Name of the author.
    - description (Optional[str]): Additional description about the author (optional).
    """
    def __init__(self, code: str, name: str, description: Optional[str] = None):
        self.code = code
        self.name = name
        self.description = description

class Constraint:
    """
    Represents a constraint for an attribute.

    Attributes:
    - code (str): Unique code identifying the constraint.
    - name (str): Name of the constraint.
    - description (Optional[str]): Additional description about the constraint (optional).
    - min_value (Optional[float]): Minimum allowed value (optional).
    - max_value (Optional[float]): Maximum allowed value (optional).
    - min_length (Optional[int]): Minimum allowed length (optional).
    - max_length (Optional[int]): Maximum allowed length (optional).
    - regex_pattern (Optional[str]): Regular expression pattern for validation (optional).
    """
    def __init__(
        self,
        code: str,
        name: str,
        description: Optional[str] = None,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex_pattern: Optional[str] = None,
    ):
        self.code = code
        self.name = name
        self.description = description
        self.min_value = min_value
        self.max_value = max_value
        self.min_length = min_length
        self.max_length = max_length
        self.regex_pattern = regex_pattern

class Attribute:
    """
    Represents an attribute of an entity.

    Attributes:
    - code (str): Unique code identifying the attribute.
    - name (str): Name of the attribute.
    - description (Optional[str]): Additional description about the attribute (optional).
    - constraint (Optional[Constraint]): Constraint associated with the attribute.
    """
    def __init__(self, code: str, name: str, description: Optional[str] = None, constraint: Optional[Constraint] = None):
        self.code = code
        self.name = name
        self.description = description
        self.constraint = constraint

class Entity:
    """
    Represents a generic data structure.

    Attributes:
    - code (str): Unique code identifying the entity.
    - name (str): Name of the entity.
    - description (Optional[str]): Additional description about the entity (optional).
    - author (Optional[Author]): Author of the entity (optional).
    - version (Optional[str]): Version of the entity (default is "1.0").
    - valid_from (Optional[datetime]): Validity start date and time (optional).
    - valid_to (Optional[datetime]): Validity end date and time (optional).
    - attributes (Dict[str, Attribute]): Dictionary of attributes associated with the entity (key is attribute code).
    """
    def __init__(
        self,
        code: str,
        name: str,
        description: Optional[str] = None,
        author: Optional[Author] = None,
        version: Optional[str] = "1.0",
        valid_from: Optional[datetime] = None,
        valid_to: Optional[datetime] = None,
    ):
        self.code = code
        self.name = name
        self.description = description
        self.author = author
        self.version = version
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.attributes: Dict[str, Attribute] = {}

    def add_attribute(self, attribute: Attribute):
        """
        Add an attribute to the entity.

        Parameters:
        - attribute (Attribute): The attribute to be added.
        """
        self.attributes[attribute.code] = attribute

class Relationship:
    """
    Represents a relationship between entities.

    Attributes:
    - entity1 (Entity): First entity in the relationship.
    - entity2 (Entity): Second entity in the relationship.
    - relationship_type (Literal['one_to_many', 'many_to_one']): Type of relationship.
    - entity1_attribute (Attribute): Attribute of the first entity for joining.
    - entity2_attribute (Attribute): Attribute of the second entity for joining.
    """
    def __init__(self, entity1: Entity, entity2: Entity, relationship_type: Literal['one_to_many', 'many_to_one'], entity1_attribute: Attribute, entity2_attribute: Attribute):
        self.entity1 = entity1
        self.entity2 = entity2
        self.relationship_type = relationship_type
        self.entity1_attribute = entity1_attribute
        self.entity2_attribute = entity2_attribute