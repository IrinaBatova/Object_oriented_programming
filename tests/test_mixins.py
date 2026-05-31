from src.mixins import ReprMixin


# Вспомогательный (мок) класс для тестирования миксина
class User(ReprMixin):

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Обеспечивает вызов следующего класса в MRO
        super().__init__()


class TestReprMixin:

    def test_repr_mixin(self):

        # Подготовка данных
        test_obj = User("Alice", 30)

        # Вызов тестируемого метода миксина
        result = test_obj.__repr__()

        assert result == "User(name='Alice', age=30)"
