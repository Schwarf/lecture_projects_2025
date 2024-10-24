from functions.helpers import fetch_data_from_db, clean_data, analyze_data, save_results


# BAD: A function that does too many things
# A so called GOD-FUNCTION
def handle_data():
    data = fetch_data_from_db()
    cleaned_data = clean_data(data)
    result = analyze_data(cleaned_data)
    save_results(result)
    return result



# GOOD: Each function does one thing
def get_data():
    return fetch_data_from_db()

def process_data(data):
    cleaned_data = clean_data(data)
    return analyze_data(cleaned_data)

def save_result(result):
    save_results(result)


# The methods in the good example should then be called e.g. like below:
def process_and_save_data():
    data = get_data()
    result = process_data(data)
    save_result(result)

# - Here the API of how the data is retrieved is hidden, because for processing and saving the
#   source of the data (e.g. a file, a database, a website ...) is not relevant
# - The same is true for the processing step. The details of the process (cleaning and analysis) are not
#   relevant and are hidden behind the process_data-API
