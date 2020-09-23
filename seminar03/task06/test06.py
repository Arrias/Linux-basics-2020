import unittest
import subprocess
import os


class Test5(unittest.TestCase):
    def print_wc_in_line(self, filename: str):
        result = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                strlen = len(line.split())
                tmp = line + " " + str(strlen)
                result.append(tmp.split())
            f.close()

        return result


    def bash_result(self, script_name: str, filename: str):
        print(script_name)
        p = subprocess.Popen(['bash', script_name, filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        stdout = stdout.decode('utf-8').split()

        return stdout
        

    def test1(self):
        script = 'task06.sh'
        filename = 'file.txt'

        bash = self.bash_result(script, filename)
        gold = self.print_wc_in_line(filename)

        print(bash)
        print(gold)

        self.assertEqual(bash, gold)



if __name__ == '__main__':
    unittest.main()
