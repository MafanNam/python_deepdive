import traceback
from datetime import datetime
from http import HTTPStatus
import json


class WidgetException(Exception):
    message = 'Generic Widget exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args, customer_message=None):
        super().__init__(args)

        if args:
            self.message = args[0]
        self.customer_message = customer_message if customer_message is not None else self.message

    @property
    def traceback(self):
        return traceback.TracebackException.from_exception(self).format()

    def log_exception(self):
        exception = {
            'type': type(self).__name__,
            'message': self.message,
            'args': self.args[1:],
            'traceback': list(self.traceback)
        }
        print(f"EXCEPTION: {datetime.utcnow().isoformat()}: {exception}")

    def to_json(self):
        response = {
            'code': self.http_status.value,
            'message': f"{self.http_status.phrase}: {self.customer_message}",
            'category': type(self).__name__,
            'time_utc': datetime.utcnow().isoformat(),
        }
        return json.dumps(response)


class SupplierException(WidgetException):
    message = 'Supplier exception'


class NotManufacturedException(SupplierException):
    message = 'Widget is no longer manufactured by supplier'


class ProductionDelayedException(SupplierException):
    message = 'Widget production has been delayed by manufactured'


class ShippingDelayedException(SupplierException):
    message = 'Widget shipping has been delayed be supplier'


class CheckoutException(WidgetException):
    message = 'Checkout exception'


class InventoryException(CheckoutException):
    message = 'Checkout inventory exception'


class OutOfStockException(InventoryException):
    message = 'Inventory out of stock'


class PricingException(CheckoutException):
    message = 'Checkout pricing exception'


class InvalidCouponCodeException(PricingException):
    message = 'Invalid checkout coupon code'


class CannotStackCouponException(PricingException):
    message = 'Cannot stack checkout coupon code'


e = WidgetException('same cust for log and user',
                    customer_message='cust user message')
print(e.log_exception())
print(json.loads(e.to_json()))







