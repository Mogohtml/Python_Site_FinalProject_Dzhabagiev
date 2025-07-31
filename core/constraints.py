from enum import Enum

class SizeEnum(str, Enum):
    XS = "Extra Small"
    S = "Small"
    M = "Medium"
    L = "Large"
    XL = "Extra Large"

class CategoryEnum(str, Enum):
    CASUAL = "Casual"
    FORMAL = "Formal"
    # Добавьте другие категории по необходимости
