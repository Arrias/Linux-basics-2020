import unittest
import subprocess
import os


class Test5(unittest.TestCase):
    def delete_blank(self, filename: str):
        result = []

        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if (line[0] != '\n'):
                    result.append(line.rstrip())
            f.close()

        return result


    def bash_result(self, script_name: str, filename: str):
        print(script_name)
        p = subprocess.Popen(['bash', script_name, filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        stdout = stdout.decode('utf-8').split()

        return stdout
        

    def test1(self):
        script = 'task05.sh'
        br = self.bash_result(script, filename='blank.txt')

        self.assertEqual(br, self.delete_blank(filename='blank.txt'))



if __name__ == '__main__':
    unittest.main()
