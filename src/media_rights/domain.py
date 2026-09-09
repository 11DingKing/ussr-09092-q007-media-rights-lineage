"""稳定的领域值和输入去重规则。"""
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class MediaRightsWindow:
    reference: str
    starts_at: datetime
    ends_at: datetime
    def duration_seconds(self) -> int:
        value = int((self.ends_at - self.starts_at).total_seconds())
        if value <= 0:
            raise ValueError("结束时间必须晚于开始时间")
        return value

def asset_ids(items: list[dict[str, object]]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        value = str(item.get("id", "")).strip()
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result
