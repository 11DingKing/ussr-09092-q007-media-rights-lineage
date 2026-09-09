def ancestors(asset_id: str, edges: dict[str, str]) -> list[str]:
    result = []
    current = asset_id
    while current in edges:
        current = edges[current]
        result.append(current)
    return result
