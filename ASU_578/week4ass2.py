

import sqlite3 as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

# 分别从attraction和checkin表格取出所有数据
#cur.execute("SELECT * FROM attraction")
#attraction_table = cur.fetchall()

cur.execute("SELECT * FROM sequences")
sequences = cur.fetchall()

# print(sequences)

TargetAttID = '8'  # 目标attractionID

TimeSlotIDList = []
CountList = []
TotalTimeSlot = 576

count = dict()
for TimeSlotID in range(TotalTimeSlot ):
    count[TimeSlotID] = 0
    TimeSlotIDList.append(TimeSlotID)


for oneline in sequences:
    Timeseq = oneline[2].split(sep = '-')
    for TimeSlotID in range(len(Timeseq)):
        if Timeseq[TimeSlotID] == TargetAttID:
            count[TimeSlotID] += 1
#print(count)

for TimeSlotID in count.keys():
    CountList.append(count[TimeSlotID])

window_size = 50

window_weights = np.ones(window_size) / window_size
ma = np.convolve(CountList, window_weights, mode='same')
plt.plot(ma)

plt.title('Moving average chart of attendance at Atmosfear Rides', fontsize = 16)
plt.xlabel('TimeSlotID', fontsize = 14)
plt.ylabel('Moving average chart of attendance', fontsize = 14)


plt.show()