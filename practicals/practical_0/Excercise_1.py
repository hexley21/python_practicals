class TestPaper():
    def __init__(self, subject: str, answers: list, barrier: str):
        self.subject = subject
        self.mark_scheme = answers
        self.pass_mark = barrier


class Student():
    test_taken = "No tests taken"

    def take_test(self, test: TestPaper, answers: list):
        barrier = int(test.pass_mark.replace('%', '')) / 100
        correct = 0
        for i, item in enumerate(test.mark_scheme):
            correct += 1 if(item == answers[i]) else 0
        correct /= len(test.mark_scheme)
        mark = round(correct * 100)
        if correct > barrier:
            result = f"Passed! ({mark}%)"
        else:
            result = f"Failed! ({mark}%)"
        if type(self.test_taken) is dict:
            self.test_taken[test.subject] = result
        else:
            self.test_taken = {test.subject: result}
