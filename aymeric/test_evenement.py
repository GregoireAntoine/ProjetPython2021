from evenement import Evenements
import os
import unittest


class EvenementTest(unittest.TestCase):
    EVENT_FILE_TEST = "tests_event.csv"

    def test_add_event(self):
        if os.path.exists(self.EVENT_FILE_TEST):
            os.remove(self.EVENT_FILE_TEST)
        events = Evenements("AYMERIC1")
        events.FILENAME_EVENTS = self.EVENT_FILE_TEST
        self.assertTrue(events.add_event("5/22/20", "Event1", 5))
        self.assertTrue(events.add_event("5/22/20", "Event2", 5))
        os.remove(self.EVENT_FILE_TEST)

    def test_already_exists(self):
        if os.path.exists(self.EVENT_FILE_TEST):
            os.remove(self.EVENT_FILE_TEST)
        events = Evenements("AYMERIC1")
        events.FILENAME_EVENTS = self.EVENT_FILE_TEST
        self.assertTrue(events.add_event("5/22/20", "Event1", 5))
        self.assertTrue(events.event_already_exists("5/22/20", "Event1"))
        self.assertFalse(events.event_already_exists("5/22/20", "Event6"))
        os.remove(self.EVENT_FILE_TEST)

    def test_remove_event(self):
        if os.path.exists(self.EVENT_FILE_TEST):
            os.remove(self.EVENT_FILE_TEST)
        events = Evenements("AYMERIC1")
        events.FILENAME_EVENTS = self.EVENT_FILE_TEST
        self.assertTrue(events.add_event("5/22/20", "Event1", 5))
        self.assertTrue(events.remove_event("5/22/20", "Event1"))
        self.assertFalse(events.remove_event("5/22/20", "Event2"))
        os.remove(self.EVENT_FILE_TEST)

if __name__ == '__main__':
    unittest.main()
