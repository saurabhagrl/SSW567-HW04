import json
import unittest
import unittest.mock
from unittest.mock import patch
from unittest import mock
from unittest.mock import Mock
from hw05a import getCommitnum, getUserRepos

import gitapi

class TestHw04a(unittest.TestCase):
        
    @patch("gitapi.githubapi",return_value=['Repo: CS-541-Artificial-Intelligence  Number of commits: 23', 'Repo: CS-546-Web-Programming  Number of commits: 12', 'Repo: CS-550  Number of commits: 1', 'Repo: CS-554  Number of commits: 30', 'Repo: CS-554-Web-Programming  Number of commits: 1', 'Repo: CS-562-DBMS2-Project  Number of commits: 2', 'Repo: CS-570-Data-Structures  Number of commits: 1', 'Repo: cs546b_group22_final_project  Number of commits: 30', 'Repo: CS555_A_Project_SpiritualBliss  Number of commits: 30', 'Repo: CSS-554-WebProgramming-II  Number of commits: 1', 'Repo: CS_554_Group_Project_The_mutables  Number of commits: 30'])
    #@patch.object(, "fetch_user_repo")
    def test_fetch_user_repo_mock_api(self, mock_fetch_user_repo):
        response_file = open('./response_fetch_user_repo.json')        
        repo_call_response = json.load(response_file)
        mock_fetch_user_repo.return_value = Mock(status_code = 200)
        mock_fetch_user_repo.return_value.json = repo_call_response
        response = gitapi.githubapi('yash171298')
        #print(response)
        self.assertEqual(response.json[0]['name'],"chatbot_ner")
        response_file.close()
       


        
if _name_ == '_main_':
    print('Running unit tests')
    unittest.main(exit=False)
