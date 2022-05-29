import datetime
from ..models import Observation

class Loader():
    def process_document():
        list = Loader.read_document('document.txt')
        for register in list:
            Loader.process_line(register)


    def read_document(path):
        '''
            This function returns a list of string lists from the input file
        '''
        list = []
        with open(path) as f:
            next(f) # Skip header
            for line in f:
                list.append(line.rstrip().split("\t"))
        return list


    def process_line(observation_list):
        '''
            This function takes a string list that represents an observation 
            (one input file line), with this information it creates an Observation 
        '''
        date,time,observatory_code,device_code,resol,device_matrix = observation_list
        width,height = resol.split('x')

        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        time = datetime.datetime.strptime(time, '%H:%M:%S').time()

        observation = Observation(date=date, time=time, observatory_code=observatory_code,
                                    device_code=device_code, 
                                    width=int(width),
                                    height=int(height), 
                                    device_matrix=device_matrix)

        observation.process_and_save()
        