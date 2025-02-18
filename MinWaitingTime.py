def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    qtime = 0
    timetotal = 0
    for i in range(len(queries)):
        timetotal += qtime
        qtime += queries[i]
    return timetotal
