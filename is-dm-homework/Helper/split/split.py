import io
import os
import logging


from Helper.tasks.tasks import read_file


def split(head, q_start, q_start2, q_finish, tail, variants, students, tasks):
    head = read_file('Data/templates/head.tex')
    q_start = read_file('Data/templates/qStart.tex')
    q_start2 = read_file('Data/templates/qStart2.tex')
    q_finish = read_file('Data/templates/qFinish.tex')
    tail = read_file('Data/templates/tail.tex')
    os.makedirs(os.path.dirname("Output/latex/main.tex"), exist_ok=True)
    out = io.open("Output/latex/main.tex", "w", encoding='utf-8')
    logging.info("Making main.tex file...")

    out.write(head)
    for i in range(len(variants)):
        out.write(q_start + str(students[i]) + q_start2)
        for taskNumber, task in enumerate(tasks):
            out.write(task[variants[i][taskNumber] - 1])
        out.write(q_finish)
    out.write(tail)
    out.close()

    out = io.open("Output/latex/dump.tex", "w", encoding='utf-8')
    logging.info("Making dump.tex file...")

    out.write(head)
    for i in range(len(tasks)):
        out.write(q_start + str(i + 1) + q_start2)
        for k in range(len(tasks[i])):
            out.write(tasks[i][k])
        out.write(q_finish)
    out.write(tail)
    out.close()

    logging.info("Done!")



