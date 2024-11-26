from enum import Enum
from typing import List, Optional

class BaseEnum(Enum):
  @classmethod
  def cases(cls) -> List['BaseEnum']:
    return [case for case in cls]

  @classmethod
  def values(cls) -> List[str]:
    return [case.value for case in cls]

  @classmethod
  def names(cls) -> List[str]:
    return [case.name for case in cls]

  @classmethod
  def from_value(cls, value: str) -> Optional['BaseEnum']:
    try:
      index = cls.values().index(value)
      return cls.cases()[index]
    except ValueError:
      return None

  @classmethod
  def from_name(cls, name: str) -> Optional['BaseEnum']:
    try:
      index = cls.names().index(name)
      return cls.cases()[index]
    except ValueError:
      return None
