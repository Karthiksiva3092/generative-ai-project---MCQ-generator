import logging
import os
from datetime import datetime

print("Starting the logger setup")

# Corrected strftime format string
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a directory for log files
log_path = os.path.join(os.getcwd(), "logs")
print(log_path)

os.makedirs(log_path, exist_ok=True)

# The log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)
print(LOG_FILEPATH)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)


# import logging
# import os
# from datetime import datetime

# print("Starting logger setup...")

# # Step 2: Generate log file name
# try:
#     LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#     print(f"Log file name generated: {LOG_FILE}")
# except Exception as e:
#     print(f"Error generating log file name: {e}")

# # Step 3: Create a directory for log files
# try:
#     log_path = os.path.join(os.getcwd(), "logs")
#     print(f"Log path set to: {log_path}")

#     if not os.path.exists(log_path):
#         os.makedirs(log_path, exist_ok=True)
#         print("Logs directory created successfully.")
#     else:
#         print("Logs directory already exists.")
# except Exception as e:
#     print(f"Error creating logs directory: {e}")

# # Step 4: Define the log file path
# try:
#     LOG_FILEPATH = os.path.join(log_path, LOG_FILE)
#     print(f"Log file path set to: {LOG_FILEPATH}")
# except Exception as e:
#     print(f"Error setting log file path: {e}")

# # Step 5: Configure the logging system
# try:
#     logging.basicConfig(
#         level=logging.INFO,
#         filename=LOG_FILEPATH,
#         format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
#     )
#     print("Logging configuration set up successfully.")
# except Exception as e:
#     print(f"Error in logging configuration: {e}")

# # Additional debug log to ensure logging is working
# try:
#     logging.info("Logger setup completed successfully.")
#     print("Logging test message recorded.")
# except Exception as e:
#     print(f"Error in logging test message: {e}")
