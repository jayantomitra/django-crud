from django.db import transaction


class SQLDBTransactions():
    def __init__(self):
        pass

    def commit(self):
        print("... Committing to DB")
        pass

    def rollback(self):
        print(".. Rolling Back")
        pass




