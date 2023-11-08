# from datetime import datetime, timezone
#
# class Account:
#     inter_rate = 0.5
#
#     def __init__(self, id, first_name, last_name, time_zone='XXX', balance=0):
#         self._id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.time_zone = time_zone
#         if balance <= 0:
#             raise Exception('Balance must be greater or equal 0')
#         self._balance = balance
#
#         self._deposit = None
#         self._transaction_id = 0
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @property
#     def deposit(self):
#         if self._deposit is None:
#             return 'Deposit is None'
#         return self._deposit
#
#     @deposit.setter
#     def deposit(self, value):
#         if value > self._balance:
#             raise ValueError('Your balance is not enough')
#         self._transaction_id += 1
#         self._deposit = value
#         self._balance -= value
#         print('Deposit: ', self.gen_confirmation_number('D', datetime.now()))
#
#     def withdraw(self, value):
#         if value > self._balance:
#             raise ValueError('Your balance is not enough')
#         self._transaction_id += 1
#         self._balance -= value
#         return f"From balance withdraw {value}. ID={self.gen_confirmation_number('W', datetime.now())}"
#
#     @classmethod
#     def interest_rate(cls, rate):
#         if rate < 0:
#             raise ValueError('Rate < 0')
#         cls.inter_rate = rate
#
#     @property
#     def deposit_interest(self):
#         return (self._balance * (self.inter_rate/100)) + self._balance
#
#     def gen_confirmation_number(self, operation, time:datetime):
#         return f"{operation}-{self._id}-{time.strftime('%Y%m%d')}-{self._transaction_id}"
#
# a = Account(140568, 'Gon', 'Friks', balance=1000)
#
# print(a.full_name)
# print(a.balance, a.deposit_interest)
# print(a.deposit)
# print(a.withdraw(50))
# a.deposit = 20
#
#


# -------------------------------------------------------------------------------------------


import numbers
import itertools
from datetime import timedelta

class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')

        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minute offset must be an integer.')

        if offset_minutes > 59 or offset_hours < -59:
            raise ValueError('Minutes offset must be between -59 and 59.')

        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self._name == other._name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)

    def __repr__(self):
        return (f"TimeZone(name='{self._name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")

# tz1 = TimeZone('ABC', -2, -15)
# print(tz1.name)
#
# from datetime import datetime
#
# dt = datetime.utcnow()
#
# print(dt + tz1.offset)


class TransactionID:
    def __init__(self, start_id):
        self._start_id = start_id

    def next(self):
        self._start_id += 1
        return self._start_id


class Account:
    # transaction_counter = TransactionID(100)
    #
    # def make_transaction(self):
    #     new_trans_id = Account.transaction_counter.next()
    #     return new_trans_id
    transaction_counter = itertools.count(100)

    def __init__(self, account_number, first_name, last_name):
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_name_and_set_name('_first_name', value, 'First Name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_name_and_set_name('_last_name', value, 'Last Name')


    def validate_name_and_set_name(self, attr_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)

# try:
#     a = Account(1234, 'Alex', 'Suck')
# except ValueError as ex:
#     print(ex)

a = Account(1234, 'Alex', 'Suck')
















