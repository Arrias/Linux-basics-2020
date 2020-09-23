import unittest
import subprocess
import os


class Test6(unittest.TestCase):
    def test1(self):
        p = subprocess.Popen(['bash', 'task06.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        stdout = stdout.decode('utf-8').split()

        result = ['<<2:https://www.w3.org/>>', '<<3:https://www.google.com/>>']        
        result = list(map(lambda href: href.replace(" ", ""), result))

        self.assertEqual(result, stdout)


if __name__ == '__main__':
    unittest.main()
