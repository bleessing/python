import subprocess


def convert_tex_to_pdf(tex_file_path):
    try:
        # Создаем команду для pdflatex
        command = ['pdflatex', tex_file_path]

        # Запускаем процесс и ждем его завершения
        subprocess.run(command, check=True)

        # Если нужно, можно добавить другие шаги (например, более чем один проход pdflatex)
        # subprocess.run(command, check=True)
        # subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



