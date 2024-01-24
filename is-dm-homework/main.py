from Helper.start.start import start
from Helper.split.split import split
from Helper.Convertation.Convert import convert_tex_to_pdf


def main():
    head, q_start, q_start2, q_finish, tail, variants, students, tasks = start()
    split(head, q_start, q_start2, q_finish, tail, variants, students, tasks)
    tex_file_path = "head.tex"
    convert_tex_to_pdf(tex_file_path)


if __name__ == "__main__":
    main()
