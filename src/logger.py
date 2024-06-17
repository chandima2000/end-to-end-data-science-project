import logging
import os
from datetime import datetime

## This log file is uniquely named based on the current date and time to
## ensure that each run of the program generates a separate log file.

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #Generating a Unique Log File Name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #creates the full path for the log file.

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

### test the logger
# if __name__ == "__main__":
#     logging.info("This is an info message")