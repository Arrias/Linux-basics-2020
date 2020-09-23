import unittest
import subprocess
import os


class Test7(unittest.TestCase):
    def test1(self):
        p = subprocess.Popen(['bash', 'task07.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        stdout = stdout.decode('utf-8')

        result = '2 1 3 4 5\n3 2 4 5 1\n4 3 5 1 2\n5 4 1 2 3\n1 5 2 3 4\n2 1 3 4 5\n'

        result = result.replace(" ", "")
        self.assertEqual(result, stdout)


if __name__ == '__main__':
    unittest.main()
