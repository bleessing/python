import os
import io


def read_tasks():
    result = []
    total_tasks = len(os.listdir('Data/tasks'))
    print(total_tasks + 1)
    for i in range(1, total_tasks):
        result.append([])
        total_variants = len(os.listdir('Data/tasks/%d' % i))
        for k in range(1, total_variants):
            result[i - 1].append(read_file('Data/tasks/%d/%d.tex' % (i, k)))
    return result


def read_file(name):
    file = io.open(name, encoding='utf-8')
    text = file.read()
    file.close()
    return text

