"""
Author Name: Saurabh Agrawal
SSW-567: SW Testing, Qual. Assur. & Maint
"""

import unittest

from githubapi import githubapi

class Testgithubapi(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(githubapi('?'), False)
    def testGithub2(self):
        self.assertEqual(githubapi('SaurabhAgrawal'), True)

if __name__ == '__main__':
    print("Test cases are running")
    unittest.main()
