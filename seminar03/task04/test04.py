import unittest
import subprocess
import os

from math import factorial


class Test4(unittest.TestCase):
    def get_ans(self, filename: str):
        result = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                numbers = line.rstrip().split()
                numbers = list(map(int, numbers))
                result += list(map(factorial, numbers))
            f.close()

        return result

    def bash_result(self, script_name: str, filename: str):
        print(script_name)
        p = subprocess.Popen(['bash', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        stdout = stdout.decode('utf-8').split()
        stdout = list(map(lambda w: w.rstrip(), stdout))
        
        return list(map(int, stdout))

    def test1(self):
        script = 'task04.sh'
        numbers = 'numbers.txt'

        self.assertEqual(self.bash_result('task04.sh', numbers), self.get_ans(numbers))


if __name__ == '__main__':
    unittest.main()
