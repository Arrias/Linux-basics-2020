import unittest
import subprocess
import os


class Test1(unittest.TestCase):
    def bash_result(self, script_name : str):
        print(script_name)
        p = subprocess.Popen(['bash', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()

        return int(stdout.decode('utf-8'))


    def test1(self):
        script = 'task01.sh'
        result = self.bash_result(script)
        
        self.assertEqual(result, os.path.getsize('./rnd.txt'))


if __name__ == '__main__':
    unittest.main()
