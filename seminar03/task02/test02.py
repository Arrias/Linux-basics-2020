import unittest
import subprocess
import os

from math import sqrt


class Test2(unittest.TestCase):
    def is_prime(self, n: int):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def bash_result(self, script_name : str):
        print(script_name)
        p = subprocess.Popen(['bash', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        number, is_prime = stdout.decode('utf-8').strip().split()
        
        return int(number), (is_prime.lower() == 'true')

    def test1(self):
        script = 'task02.sh'
        n, p = self.bash_result(script)

        self.assertEqual(p, self.is_prime(n))


if __name__ == '__main__':
    unittest.main()
