from datetime import datetime, timedelta


def daterange(base: datetime = datetime.now(), days=7):
    return [base + timedelta(days=x) for x in range(days)]
