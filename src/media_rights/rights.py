from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass(frozen=True)
class Right:
    asset_id: str
    expires_on: Optional[date]
    withdrawn: bool = False

    def active(self, on: date) -> bool:
        return not self.withdrawn and (self.expires_on is None or on <= self.expires_on)
