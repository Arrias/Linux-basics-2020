import unittest
import subprocess
import os

from math import gcd


class Test3(unittest.TestCase):
    def bash_result(self, script_name : str):
        print(script_name)
        p = subprocess.Popen(['bash', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        stdout = stdout.decode('utf-8').split()
        a, b, g = list(map(int, stdout))

        return a, b, g

    def test1(self):
        script = 'task03.sh'
        a, b, g = self.bash_result(script)

        self.assertEqual(g, gcd(a, b))


if __name__ == '__main__':
    unittest.main()
