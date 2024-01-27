import io


def read_students():
    file = io.open("Data/students.txt", encoding='utf-8')
    result = file.readlines()
    file.close()
    return result
