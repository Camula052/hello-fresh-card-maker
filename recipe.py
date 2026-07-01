from dataclasses import dataclass, field


@dataclass
class Recipe:

    title: str = ""
    subtitle: str = ""

    servings: int = 3

    ingredients: list = field(default_factory=list)
    tools: list = field(default_factory=list)
    steps: list = field(default_factory=list)
    images: list = field(default_factory=list)