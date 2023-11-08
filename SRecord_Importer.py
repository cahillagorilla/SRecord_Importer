'''
************************** CREATED BY ANDREW CAHILL, 08NOV2023 FOR DEVELOPMENTAL / BENCHTOP UTILITY ********************************

The purpose of this code is to import an s record into the python workspace into a workable format. The workable format is a list of 
S records, with the length of the list the same length as the number of lines in the s record file. 


'''


import bincopy

def Srec_Line_List(srec_file):
    # this function is meant to take a filename, and output a list of all the record lines

    file = bincopy.BinFile(srec_file)

    srec_list = []
    srec_string = ''
    idx = 0
    for charac in file.as_srec():
        if charac == 'S':
            if idx == 0:
                srec_string += charac
                idx += 1

            else:
                srec_list.append(srec_string)
                srec_string = 'S'

        else:
            srec_string += charac
    
    return srec_list


