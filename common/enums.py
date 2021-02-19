from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)



class UserRole(ChoiceEnum):
    SUPER_ADMIN = 1
    TEACHER = 2
    STUDENT = 3


class TypeCuestion(ChoiceEnum):
    BOOLEAN = 1
    ONE_CORRECT = 2
    MORE_ONE_CORRECT = 3
    ALL_MUST_CORRECT = 4

