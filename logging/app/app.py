# import logging

# # Logging setting
# # Configure logging to write to a file
# logging.basicConfig(
#     filename='app.log',
#     filemode='w',  # 'w' for overwrite, 'a' for append
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers = [
#         logging.FileHandler("app1.log"), 
#         logging.StreamHandler()
#     ]
# )

# logger = logging.getLogger("Arithmetic App")

# def add(a,b):   
#     result = a+b
#     logger.debug(f"Adding {a}+{b} = {result}")
#     return result

# def sub(a,b):   
#     result = a-b
#     logger.debug(f"Adding {a}-{b} = {result}")
#     return result

# def mul(a,b):   
#     result = a*b
#     logger.debug(f"Adding {a}*{b} = {result}")
#     return result

# def div(a,b):
#     try:   
#         result = a/b
#         logger.debug(f"Adding {a}/{b} = {result}")
#         return result
#     except ZeroDivisionError:
#         logger.error("Error: Division by zero is not allowed")
#         return None

# add(10,15)
# sub(10,15)
# mul(10,15)
# div(10,0)

import logging

# Create a custom logger
logger = logging.getLogger("Arithmetic App")
logger.setLevel(logging.DEBUG)  # Set level at the logger level

# Create handlers
file_handler = logging.FileHandler("app1.log", mode='w')
console_handler = logging.StreamHandler()

# Set format for both handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Arithmetic functions
def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def mul(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def div(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Error: Division by zero is not allowed")
        return None

# Test
add(10, 15)
sub(10, 15)
mul(10, 15)
div(10, 0)
add(12,15)
div(12,12)