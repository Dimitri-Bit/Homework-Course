attendence = "80%"
work_done = 1

attendence_num = int(attendence[0:2])

if attendence_num >= 75 and work_done >= 1:
    print("student approved")
else:
    print("student not approved")