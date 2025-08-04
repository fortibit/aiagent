import os
import unittest
from functions.get_files_info import get_files_info

main_py_size = os.path.getsize("./main.py")
tests_py_size = os.path.getsize("./tests.py")
calculator_main_py_size = os.path.getsize("./calculator/main.py")
calculator_tests_py_size = os.path.getsize("./calculator/tests.py")
calculator_pkg_size = os.path.getsize("./calculator/pkg")
calculator_calculator_py_size = os.path.getsize("./calculator/pkg/calculator.py")
calculator_render_py_size = os.path.getsize("./calculator/pkg/render.py")

class TestGetFilesInfo(unittest.TestCase):

    def test_current_directory(self):
        result = f"Result for current directory:\n - main.py: file_size={calculator_main_py_size} bytes, is_dir=False\n - tests.py: file_size={calculator_tests_py_size} bytes, is_dir=False\n - pkg: file_size={calculator_pkg_size} bytes, is_dir=True"
        func_result = get_files_info("calculator", ".")
        self.assertEqual(func_result, result)


if __name__ == "__main__":
    unittest.main()