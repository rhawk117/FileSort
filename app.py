from pathlib import Path
import sys 
import os 
from prog_prompts import ProgPrompts
from common import StartUp


class App:
    def __init__(self):
        self.prog_dir = None
        self.config_dir = None
        self.found_configs = []
        self.have_configs = (len(self.found_configs) > 0)
        
        self.prog_dir, self.config_dir = StartUp.start_script()


       
   
 

    



        
