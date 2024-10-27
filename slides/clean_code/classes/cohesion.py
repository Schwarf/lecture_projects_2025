# BAD EXAMPLE
class OrderProcessor:
    def __init__(self, order_data):
        self.order_data = order_data

    # Order validation logic
    def validate_order(self):
        # Code to validate order data
        pass

    # Totals calculation logic
    def calculate_totals(self):
        # Code to calculate the order total
        pass

    # Invoice generation logic
    def generate_invoice_pdf(self):
        # Code to generate a PDF invoice for the order
        pass

    # Notification logic
    def send_confirmation_email(self, email_address):
        # Code to send a confirmation email to the customer
        pass

    def send_invoice_email(self, email_address):
        # Code to send the invoice as an email
        pass


# GOOD EXAMPLE

class Order:
    def __init__(self, order_data):
        self.data = order_data


class OrderValidator:
    def validate(self, order: Order) -> bool:
        # Code to validate the order
        return True  # Simplified for demonstration


class OrderCalculator:
    def calculate_totals(self, order: Order) -> float:
        # Code to calculate totals
        return 100.0  # Placeholder total for demonstration


class InvoiceGenerator:
    def generate_pdf(self, order: Order) -> bytes:
        # Code to generate PDF content for the invoice
        return b"%PDF-1.4..."  # Placeholder PDF content


class NotificationService:
    def send_confirmation_email(self, email_address: str, order: Order) -> None:
        # Code to send a confirmation email
        print(f"Sending confirmation email to {email_address}")

    def send_invoice_email(self, email_address: str, invoice_pdf: bytes) -> None:
        # Code to send the invoice PDF by email
        print(f"Sending invoice email to {email_address}")


# Using the classes together in a process

class OrderProcessor:
    def __init__(self, order: Order):
        self.order = order
        self.validator = OrderValidator()
        self.calculator = OrderCalculator()
        self.invoice_generator = InvoiceGenerator()
        self.notification_service = NotificationService()

    def process_order(self, email_address: str):
        if not self.validator.validate(self.order):
            print("Order validation failed.")
            return

        total = self.calculator.calculate_totals(self.order)
        print(f"Order total calculated: {total}")

        invoice_pdf = self.invoice_generator.generate_pdf(self.order)
        self.notification_service.send_confirmation_email(email_address, self.order)
        self.notification_service.send_invoice_email(email_address, invoice_pdf)
