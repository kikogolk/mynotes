import unittest
import mock

class MyTest(unittest.TestCase):
    def test_non_existing_module(self):
        non_existing_module_mock = mock.MagicMock()
        with mock.patch.dict('sys.modules', {'non_existing_module': non_existing_module_mock}):
            from sut import MyClass

            non_existing_module_mock.get_non_existing_attr = mock.MagicMock()
            non_existing_module_mock.get_non_existing_attr.return_value = "HELLO"

            myclass = MyClass()
            value = myclass.get_non_existing_attr()

            self.assertEquals(value, "attr1HELLO")
