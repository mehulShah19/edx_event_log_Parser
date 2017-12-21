course_date_dict_fileName = "date_dictionary.json"


# Format = yyyy-MM-dd

# Inclusive Start and End Date
start_date = "2017-08-08"
end_date = "2017-08-10"

# Add / in the end
folder_path = "/Users/edplus/Desktop/edx/"


courses_list = [
    "ASUx+ECN211x+2177A",
    "ASUx+MAT117x+1T2016"
]

# File Structure of the input file which needs to be parsed
eventlog_file_structure = [
                    'username',
                    ('context','user_id'), # Nested Json Parsing
                    ('context','course_id'),
                    'time',
                    'event',
                    'event_type',
                    'page'

                    ]

# Header List of the csv file
eventlog_headerList = ["username",
              "user_id",
              "course_id",
              "time",
              "event",
              "event_type",
              "page"]

