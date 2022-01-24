from utilisateur import Utilisateur
import os
import unittest


class UtilisateurTest(unittest.TestCase):
    AUTH_FILE_TEST = "tests_auth.csv"

    def test_create_user(self):
        if os.path.exists(self.AUTH_FILE_TEST):
            os.remove(self.AUTH_FILE_TEST)
        self.user = Utilisateur("AYMERIC1", "aymeric1")
        self.user.FILE_NAME = self.AUTH_FILE_TEST
        self.assertTrue(self.user.create_user())
        self.user2 = Utilisateur("AYMERIC2", "aymeric2")
        self.user2.FILE_NAME = self.AUTH_FILE_TEST
        self.assertTrue(self.user2.create_user())
        self.user3 = Utilisateur("AYMERIC1", "aymeric1")
        self.user3.FILE_NAME = self.AUTH_FILE_TEST
        self.assertFalse(self.user3.create_user())
        os.remove(self.AUTH_FILE_TEST)

    def test_username_exists(self):
        if os.path.exists(self.AUTH_FILE_TEST):
            os.remove(self.AUTH_FILE_TEST)
        self.user = Utilisateur("AYMERIC1", "aymeric1")
        self.user.FILE_NAME = self.AUTH_FILE_TEST
        self.assertTrue(self.user.create_user())
        self.assertTrue(self.user.username_exists())
        self.user2 = Utilisateur("AYMERIC2", "aymeric2")
        self.user.FILE_NAME = self.AUTH_FILE_TEST
        self.assertFalse(self.user2.username_exists())
        os.remove(self.AUTH_FILE_TEST)

    def test_bind(self):
        if os.path.exists(self.AUTH_FILE_TEST):
            os.remove(self.AUTH_FILE_TEST)
        self.user = Utilisateur("AYMERIC1", "aymeric1")
        self.user.FILE_NAME = self.AUTH_FILE_TEST
        self.assertTrue(self.user.create_user())
        self.assertTrue(self.user.bind())
        self.user2 = Utilisateur("AYMERIC2", "aymeric2")
        self.user2.FILE_NAME = self.AUTH_FILE_TEST
        self.assertFalse(self.user2.bind())
        os.remove(self.AUTH_FILE_TEST)


if __name__ == '__main__':
    unittest.main()
