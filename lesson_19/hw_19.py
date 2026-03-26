from datetime import datetime

KEY = "TSTFEED0300|7E3E|0400"

with open("hblog.txt") as file:
    lines = file.readlines()

filtered_log = []
for line in lines:
    if KEY in line:
        filtered_log.append(line)

times = []
for line in filtered_log:
    position = line.find("Timestamp ")
    if position != -1:
        time_str = line[position + 10:position + 18]
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        times.append(time_obj)

with open("hb_test.log", "w") as log:
    for i in range(len(times) - 1):
        t1 = times[i]
        t2 = times[i + 1]

        difference = abs((t1 - t2).total_seconds())

        if 31 < difference < 33:
            log.write(f"WARNING: heartbeat = {difference}s at {t1:%H:%M:%S}\n")
        elif difference >= 33:
            log.write(f"ERROR: heartbeat = {difference}s at {t1:%H:%M:%S}\n")