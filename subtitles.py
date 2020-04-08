import datetime

with open("Mr.Robot.srt", 'r') as s:
    subtitle_list = s.read()

try:
    finall_subtr = []
    subtitle = subtitle_list.split("\n\n")[1:]
    for elements_subtile in subtitle:
        lines = elements_subtile.split("\n")
        elements_time = lines[1].split(" --> ")
        for element in elements_time:
            element_first = datetime.datetime.strptime(elements_time[0], "%H:%M:%S,%f")
            element_second = datetime.datetime.strptime(elements_time[1], "%H:%M:%S,%f")
            newdt_1 = element_first + datetime.timedelta(seconds=2)
            newdt_2 = element_second + datetime.timedelta(seconds=2)
            new_time = str(newdt_1.time().replace(microsecond=0)), str(
             newdt_2.time().replace(microsecond=0))
            new_time_list = list(new_time)
        join_time_elements = (" --> ").join(new_time)
        lines[1] = join_time_elements
        finall_sub = ("\n").join(lines)
        finall_subtr.append('\n{}'.format(finall_sub))


except Exception:
    print("end")


with open("new_filename.srt", 'a') as f:
    f.write(finall_subtr[0])
    for s in finall_subtr:
        f.write('\n{0}'.format(s))
