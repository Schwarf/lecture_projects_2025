# BAD: What does this class and method represent?
class Processor:
    def process(self, l):
        pass



# BETTER: More descriptive, but not perfect
class DataProcessor:
    def process_list(self, lst):
        pass



# GOOD: Intent is immediately clear
class RevenueCalculator:
    def calculate_annual_revenue(self, transactions):
        pass

