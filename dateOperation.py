from datetime import  datetime


class Date_Operation:

    def get_date_from_fileName(self, fileName):
        if(fileName is None or len(fileName) == 0):
            return None

        # asux-edx-events-2017-08-08.log.gz
        if not "." in fileName:
            return None

        init = fileName.split(".")[0]

        if(len(init) < 10):
            return None

        date_string = init[-10:]
        if(self.validate_date(date_string)):
            return date_string
        else:
            None



    def validate_date(self,d):
        try:
            datetime.strptime(d, '%Y-%m-%d')
            return True
        except ValueError:
            return False



dateOperation = Date_Operation()

#print(dateOperation.get_date_from_fileName("asux-edx-events-2017-08-08.log.gz"))