from typing import Callable

class TestCase:

    def __init__(self, test_method_name: str) -> None:
        self.test_method_name = test_method_name

    def run(self) -> None:
        self.set_up()
        try:
            test_method: Callable[[], None] = getattr(self, self.test_method_name)
            test_method()
        finally:
    
            self.tear_down()

    def set_up(self) -> None:
        pass

    def tear_down(self) -> None:
        pass