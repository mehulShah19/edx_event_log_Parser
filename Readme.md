### Edx Event Log Parser

This repository contains code to parse the event log daily data obtained from the edx-platform

Used **Python 2.7** in building this application

Libraries required are 
    gzip, datetime, json, csv, io, os 
    - Most libraries will be bundled with the python language
   
   
#### Constant.py
    This file contains the parameters which can be used to customize the parser, following parameters will provide the flexibility
    
1. Start_time/End_time - To select the edx folder of parsing
2. folder_path - Location where the input file resides
3. courses_list - List of the courses whose data needs to be parsed
4. eventlog_file_structure - This is the file structure used to parse the input file. This can be modified depending on the need of the researcher
5. eventlog_headerList - This file contains the header field name of the output csv file


#### event_parsing_main.py 
    This file is the starting point of the application where the core parsing is written and should be called to begin the parser
