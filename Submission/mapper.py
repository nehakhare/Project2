#!/usr/bin/env python
import sys

def mapToDict(ls):
    return {'Id':ls[0],
            'Date':ls[1],
            'Type':ls[2],
            'Value':ls[3],
            'MFlag':ls[4],
            'QFlag':ls[5],
            'SFlag':ls[6],
            'OBSTime':ls[7]}

for line in sys.stdin:
    parse = line.strip().upper().split(',')
    row = mapToDict(parse)
    if 'TMAX' != row['TYPE'] and 'TMIN' != row['TYPE']:
        continue
    if row['Value'] == -9999:
        continue
    if row['SFlag'] == '':
        continue
    if row['QFlag'] != '':
        continue
    if row['MFlag'] == 'P':
        contiune
    print '%s,%s,%s,%s,' % (row['Date'],row['Id'],row['Type'],row['Value'])