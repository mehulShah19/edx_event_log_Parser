import os.path
from os import listdir
from os.path import isfile, join
import os
import Constant
import json
import csv

class FileFolderOperation:

    '''
    This method checks if the Folder  is Present
    It returns boolean
    '''

    def isFolderPresent(self, path):
        if(path is None or len(path) == 0):
            return False

        if(not os.path.isdir(path)):
            return False
        return True


    '''
    This method goes to the folder path mentioned in the folderPath
    and returns the list of all the files name ending with .gz
    '''

    def get_list_of_files_with_gz_file_type(self, folderPath):
        list_of_gzip_files = []
        if not self.isFolderPresent(folderPath):
            return list_of_gzip_files

        for f in listdir(folderPath):
            if ".gz" in f and isfile(join(folderPath, f)) :
                list_of_gzip_files.append(f)

        return list_of_gzip_files


    '''
    This method will pull all the courses and dates which are already parsed
    This will help in removing the duplicacy in the dataset
    '''
    def get_stored_course_date_map(self, folder_path):
        course_date_map = {}

        if not os.path.isfile(folder_path + Constant.course_date_dict_fileName):
            return course_date_map

        with open(folder_path + Constant.course_date_dict_fileName,'r') as f:
            course_date_map = json.load(f)

        return course_date_map
        pass

    '''
        This method stores all the course and the dates which are parsed
        This will help in removing the duplicacy in the dataset
        '''

    def store_course_date_map(self, folder_path, course_date_map):
        if (course_date_map is None):
            return

        with open(folder_path + Constant.course_date_dict_fileName, "w") as f:
            json.dump(course_date_map, f)


    '''
    This method will store the csvList on the filePathLocation
    If filePathLocation is not present than the header list is being added in the file
    or else only the content will be added
    There is no check of the data duplicacy this method will just add data to the file
    '''
    def csv_store(self, folder_path, file_name, csv_list, header_list):
        filePath = join(folder_path, file_name)

        isFilePresent = os.path.isfile(filePath)
        if (isFilePresent):
            with open(filePath, 'a') as csvfile:
                writer = csv.writer(csvfile)
                for row in csv_list:
                    writer.writerow(row)
        else:
            with open(filePath, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header_list)
                for row in csv_list:
                    writer.writerow(row)

        return True



