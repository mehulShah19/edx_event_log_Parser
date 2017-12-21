import Constant
import fileFolderOperation
import dateOperation
import gzip
import json
import io

class Edx_event_parsing:

    # Starting point of the class call
    # Initializing all the classes used for parsing
    file_folder_operation = fileFolderOperation.FileFolderOperation()
    date_operation = dateOperation.Date_Operation()
    course_date_map = file_folder_operation.get_stored_course_date_map(Constant.folder_path)

    # This method is the starting point for the parsing
    def startParsing(self):
        # Default date to include all the files if not mentioned in the Constant.py file
        start_time = "1900-01-01"
        end_time = "2100-01-01"


        if (Constant.start_date is not None and self.date_operation.validate_date(Constant.start_date) == True):
            start_time = Constant.start_date

        if (Constant.end_date is not None and self.date_operation.validate_date(Constant.end_date) == True):
            end_time = Constant.end_date

        print("Start Time ", start_time)
        print("End Time ", end_time)

        if not self.file_folder_operation.isFolderPresent(Constant.folder_path):
            return

        list_of_files = self.file_folder_operation.get_list_of_files_with_gz_file_type(Constant.folder_path)

        for course_id in Constant.courses_list:
            # print course_id

            for fileName in list_of_files:
                date_of_file_name = self.date_operation.get_date_from_fileName(fileName)
                # print("File in Date ", date_of_file_name)
                # Check if the file Name is in the format <xx>-yyyy-mm-dd.json.gz
                if(date_of_file_name is None):
                    continue


                if not (date_of_file_name >= start_time and date_of_file_name <= end_time) :
                    continue

                if self.is_date_already_parsed(course_id, date_of_file_name):
                    continue

                filePath = Constant.folder_path + fileName

                #csv_list = self.parse_file("/Users/edplus/Desktop/edx/asux-edx-events-2017-09-01.log.gz", course_id, Constant.py.eventlog_file_structure)

                csv_list = self.parse_file(filePath, course_id, Constant.eventlog_file_structure)

                print "Count" , len(csv_list)
                # print csv_list
                if csv_list is None:
                    continue

                self.file_folder_operation.csv_store(Constant.folder_path,course_id + ".csv", csv_list, Constant.eventlog_headerList)

                if course_id not in self.course_date_map:
                    self.course_date_map[course_id] = [date_of_file_name]
                else:
                    self.course_date_map[course_id].append(date_of_file_name)

                self.file_folder_operation.store_course_date_map(Constant.folder_path, self.course_date_map)


    def parse_file(self,file_path, course_id, file_structure):
        print ("Inside Parser1", file_path)
        csv_rows_list = []
        gz = gzip.open(file_path, 'rb')
        f = io.BufferedReader(gz)
        for line in f.readlines():
            json_line = json.loads(line)
            # Check courseName

            if "context" not in json_line or "course_id" not in json_line['context'] or course_id not in \
                    json_line['context']['course_id']:
                continue

            row = []
            for struct in file_structure:
                single_item = ""
                json_struct = json_line

                if type(struct) is str:
                    if struct in json_struct:
                        single_item = json_struct[struct]

                else:
                    for i in range(0, len(struct), 1):
                        if json_struct is None:
                            break

                        if (i == len(struct) - 1 and struct[i] in json_struct):
                            single_item = json_struct[struct[i]]

                        else:
                            if (struct[i] in json_struct):
                                json_struct = json_struct[struct[i]]

                row.append(single_item)
            # print row
            csv_rows_list.append(row)
        f.close()
        gz.close()

        return csv_rows_list


    def is_date_already_parsed(self, courseName, date):
        if self.course_date_map == None or len(self.course_date_map) == 0 :
            return False

        if not courseName in self.course_date_map.keys():
            return False

        if date in self.course_date_map[courseName]:
            return True

        return False


edx = Edx_event_parsing()
edx.startParsing()
#edx.parse_file("/Users/edplus/Dropbox (ASU)/ENC 211 Event Data/tracklog-2017-08-14.json.gz", Constant.py.courses_list[0],Constant.py.eventlog_file_structure)