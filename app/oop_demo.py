from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Task:
    id: int
    title: str


class ValidationError(ValueError):
    """Błąd walidacji danych wejściowych."""
    pass


class Validator:
    """Klasa bazowa – każdy walidator musi mieć metodę validate()."""

    def validate(self, data: Dict[str, Any]) -> None:
        raise NotImplementedError


class TaskRequiredFieldsValidator(Validator):
    def validate(self, data: Dict[str, Any]) -> None:
        if "id" not in data or "title" not in data:
            raise ValidationError("Missing required fields: id, title")


class TaskTypesValidator(Validator):
    def validate(self, data: Dict[str, Any]) -> None:
        if not isinstance(data.get("id"), int):
            raise ValidationError("id must be int")
        if not isinstance(data.get("title"), str):
            raise ValidationError("title must be str")


class TaskParser:
    """Klasa, która używa walidatorów i buduje obiekt Task."""

    def __init__(self, validators: list[Validator]) -> None:
        self.validators = validators

    def parse(self, data: Dict[str, Any]) -> Task:
        if not isinstance(data, dict):
            raise ValidationError("Input must be a dict")

        for validator in self.validators:
            validator.validate(data)

        return Task(
            id=data["id"],
            title=data["title"],
        )


if __name__ == "__main__":
    parser = TaskParser(
        validators=[
            TaskRequiredFieldsValidator(),
            TaskTypesValidator(),
        ]
    )

    good_data = {"id": 1, "title": "Learn HTTP"}
    bad_data = {"id": "one", "title": 123}

    print("GOOD:")
    print(parser.parse(good_data))

    print("\nBAD:")
    try:
        parser.parse(bad_data)
    except ValidationError as e:
        print(e)
