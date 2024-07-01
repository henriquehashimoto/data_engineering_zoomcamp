
# This will be the pipeline file that docker will import to use
import pandas as pd 
import sys 

# Pipeline of data
print(sys.argv)
day = sys.argv[1] # Receive and argument passed


# Message
print(f'Job executed succesfully on the day: {day}')

