
import random
import logging
from Helper.tasks.tasks import read_tasks, read_file
from Helper.students.students import read_students
from Helper.variants.variant import generate_variants


def start():
    random.seed(1183)
    logging.info("Reading templates...")
    head = read_file('templates/head.tex')
    q_start = read_file('templates/qStart.tex')
    q_start2 = read_file('templates/qStart2.tex')
    q_finish = read_file('templates/qFinish.tex')
    tail = read_file('templates/tail.tex')

    logging.info("Reading tasks...")
    tasks = read_tasks()

    logging.info("Reading students...")

    students = read_students()

    logging.info("Generating variants...")
    variants = generate_variants(tasks, len(students))
    random.shuffle(variants)

    return head, q_start, q_start2, q_finish, tail, variants, students, tasks,
