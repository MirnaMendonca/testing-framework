from xunit import TestCase
from xunit.testresult import TestResult

class MyTest(TestCase):
    def set_up(self):
        self.x = 1

    def tear_down(self):
        pass

    def test_pass(self):
        assert self.x == 1

    def test_fail(self):
        assert self.x == 2

    def test_error(self):
        1 / 0

if __name__ == "__main__":
    result = TestResult()
    for name in ("test_pass", "test_fail", "test_error"):
        MyTest(name).run(result)
    print(result.summary())
