class Sender:
    cnt = True
    @classmethod
    def report(cls):
        if cls.cnt:
            cls.cnt = False
            return 'Greetings'
        return 'Get away'

class Asker:
    @staticmethod
    def askall(lst):
        return [i.report() for i in lst]
