from enums.core.base_num import BaseEnum
from typing import Dict

class DualOption(BaseEnum):
  YES = 'y'
  NO = 'n'

  def to_str(self) -> str:
    strs: Dict[DualOption, str] = {
      DualOption.YES: 'yes',
      DualOption.NO: 'no',
    }

    return strs[self]
