###Edx Event Log Parser

This repository contains code to parse the event data obtained from the edx-platform

Used **Python 2.7** in building this application

Libraries required are 
    gzip, datetime, json, csv, io, os 
    - Most will be bundled with the python language
   

####Constant.py
    This file contains the parameters which can be used to customize the parser
    
Following parameters will provide the flexibility of customization
1. Start_time/End_time - To select the edx folder of parsing
2. folder_path - This path contains the input file obtained from the edx platform
3. courses_list - This contains list of the courses whose data needs to be parsed
4. eventlog_file_structure - This is the file structure of the input file used for parsing fields depending on the needs of the parser
5. eventlog_headerList - This file contains the header list of the output csv file


####event_parsing_main.py 
    This file is the starting point of the application where the core parsing is written
