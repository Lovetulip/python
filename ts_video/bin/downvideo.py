

#__author__ : tuple
#__data____ : 20180815

import os 
import sys 

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from core import ui 



if __name__ == "__main__":
    ui.run()