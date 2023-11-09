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
from datetime import datetime
from collections import namedtuple


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


# class TransactionID:
#     def __init__(self, start_id):
#         self._start_id = start_id
#
#     def next(self):
#         self._start_id += 1
#         return self._start_id


class Account:
    # transaction_counter = TransactionID(100)
    #
    # def make_transaction(self):
    #     new_trans_id = Account.transaction_counter.next()
    #     return new_trans_id
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5

    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X',
    }

    def __init__(self, account_number, first_name, last_name,
                 timezone=None, initial_balance=0):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone

        self._balance = float(initial_balance)

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

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def balance(self):
        return self._balance

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time Zone must be a valid TimeZone object.')
        self._timezone = value

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number.')

        if value < 0:
            raise ValueError('Interest rate cannot be negative.')
        cls._interest_rate = value

    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')
        if min_value is None and value < min_value:
            raise ValueError('Value must be a positive number.')
        return value

    def generate_confirmation_code(self, transaction_code):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f"{transaction_code}-{self._account_number}-{dt_str}-{next(Account.transaction_counter)}"

    def validate_name_and_set_name(self, attr_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)

    def make_transaction(self):
        return self.generate_confirmation_code('dummy')

    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            raise ValueError('Invalid conformation code.')

        transaction_code, account_number, raw_dt_utc, transaction_id = parts

        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError as ex:
            raise ValueError('Invalid transaction datetime.') from ex

        if preferred_time_zone is None:
            preferred_time_zone = TimeZone('UTC', 0, 0)

        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Invalid TimeZone specified.')

        dt_preferred = dt_utc + preferred_time_zone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

        return Confirmation(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str)

    def deposit(self, value):
        value = Account.validate_real_number(value, 0.01)
        transaction_code = Account._transaction_codes['deposit']
        conf_code = self.generate_confirmation_code(transaction_code)
        self._balance += value
        return conf_code

    def withdraw(self, value):
        value = Account.validate_real_number(value, 0.01)

        accepted = False
        if self._balance - value < 0:
            transaction_code = Account._transaction_codes['rejected']
        else:
            accepted = True
            transaction_code = Account._transaction_codes['withdraw']

        conf_code = self.generate_confirmation_code(transaction_code)

        if accepted:
            self._balance -= value

        return conf_code

    def pay_interest(self):
        interest = self._balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(Account._transaction_codes['interest'])
        self._balance += interest
        return conf_code


Confirmation = namedtuple('Confirmation', 'account_number transaction_code transaction_id time_utc time')



# try:
#     a = Account(1234, 'Alex', 'Suck')
# except ValueError as ex:
#     print(ex)
#
# try:
#     a = Account(1234, '', '', '-7:00')
# except ValueError as ex:
#     print(ex)
#
# print(a.timezone)
# a.timezone = '-7:00'
# print(Account.get_interest_rate())

# a = Account('A100', 'Eric', 'Idle')
# conf_code = a.make_transaction()
# print(conf_code)
# print(Account.parse_confirmation_code(conf_code))
#
#
#
# print(a.make_transaction())
# a2 = Account('A100', 'Eric', 'Idle')
# print(a2.make_transaction())
# print(a2.make_transaction())

a = Account('A100', 'Eric', 'Idle', initial_balance=100)

print(a.balance)

print(a.deposit(50))

print(a.balance)

# print(a.withdraw(150))
print(a.pay_interest())

print(a.balance)















