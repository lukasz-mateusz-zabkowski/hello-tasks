from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    description: Optional[str] = None

def parse_task(data: dict) -> Task:
    # 1. Czy to w ogóle jest dict?
    if not isinstance(data, dict):
        raise ValueError("Input must be a dict")

    # 2. Czy są wymagane pola?
    if "id" not in data or "title" not in data:
        raise ValueError("Missing required fields: id, title")

    # 3. Czy mają poprawne typy?
    if not isinstance(data["id"], int):
        raise ValueError("id must be int")

    if not isinstance(data["title"], str):
        raise ValueError("title must be str")

    # 4. Tworzymy obiekt Task
    return Task(
        id=data["id"],
        title=data["title"],
        completed=data.get("completed", False),
        description=data.get("description"),
    )

if __name__ == "__main__":
    good_data = {
        "id": 1,
        "title": "Learn Python",
        "completed": False,
    }

    bad_data = {
        "title": "Missing ID"
    }

    print("GOOD DATA:")
    task = parse_task(good_data)
    print(task)

    print("\nBAD DATA:")
    try:
        parse_task(bad_data)
    except ValueError as e:
        print(f"Error: {e}")
