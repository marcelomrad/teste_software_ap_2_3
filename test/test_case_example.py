from src.core.test_case import TestCase
from src.core.test_result import TestResult


class MyTest(TestCase):
    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')


if __name__ == "__main__":
    result = TestResult()

    test = MyTest('test_a')
    test.run(result)

    test = MyTest('test_b')
    test.run(result)

    test = MyTest('test_c')
    test.run(result)

    print(result.summary())
