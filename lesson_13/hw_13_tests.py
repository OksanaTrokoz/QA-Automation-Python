import unittest
from homework_log import log_event

LOGGER_NAME = "log_event"

class TestLogEvent(unittest.TestCase):
    def test_withSuccessStatus_logsInfoMessage(self):
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("Oksana", "success")

        expected_message = "Login event - Username: Oksana, Status: success"
        expected_level = "INFO"

        self.assertEqual(1, len(log.records))

        record = log.records[0]
        self.assertEqual(expected_level, record.levelname)
        self.assertEqual(expected_message, record.getMessage())

    def test_withFailedStatus_logsErrorMessage(self):
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("Oksana1", "failed")

        expected_message = "Login event - Username: Oksana1, Status: failed"
        expected_level = "ERROR"

        self.assertEqual(1, len(log.records))

        record = log.records[0]
        self.assertEqual(expected_level, record.levelname)
        self.assertEqual(expected_message, record.getMessage())

    def test_withExpiredStatus_logsWarningMessage(self):
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("Tito", "expired")

        expected_message = "Login event - Username: Tito, Status: expired"
        expected_level = "WARNING"

        self.assertEqual(1, len(log.records))

        record = log.records[0]
        self.assertEqual(expected_level, record.levelname)
        self.assertEqual(expected_message, record.getMessage())

    @unittest.skip('Message log with Invalid status')
    def test_withUnknownStatus_logsNothing(self):
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("expired", "John")

        self.assertEqual(0, len(log.records))

    @unittest.skip('Status is case insensitive')
    def test_caseInsensitiveStatus(self):
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("Oksana", "SUCCESS")

        expected_message = "Login event - Username: Oksana, Status: SUCCESS"
        expected_level = "INFO"

        self.assertEqual(1, len(log.records))

        record = log.records[0]
        self.assertEqual(expected_level, record.levelname)
        self.assertEqual(expected_message, record.getMessage())

if __name__ == '__main__':
    unittest.main()
