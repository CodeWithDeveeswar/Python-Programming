import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='Python Logging/app.log', # You can remove this line to log to console
    filemode='w'
)

def divide(a, b):
    logging.info(f"Dividing {a} and {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Tried to divide by zero!")
        return None

# Test
divide(10, 5)
divide(10, 0)
