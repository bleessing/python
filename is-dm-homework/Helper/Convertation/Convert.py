import os
import subprocess


def latex_to_pdf(latex_code, output_path='output.pdf'):
    # Создаем временный файл .tex
    with open('temp.tex', 'w') as f:
        f.write(latex_code)

    # Вызываем pdflatex для компиляции .tex в .pdf
    subprocess.run(['pdflatex', '-output-directory', '.', 'temp.tex'])

    # Перемещаем результат в указанный выходной файл
    os.rename('temp.pdf', output_path)

    # Удаляем временные файлы
    os.remove('temp.tex')
    os.remove('temp.aux')
    os.remove('temp.log')

# Пример использования
latex_code = """
\\documentclass{article}
\\begin{document}
Hello, this is a simple LaTeX to PDF conversion!
\\end{document}
"""

latex_to_pdf(latex_code)
print("Conversion complete. Check output.pdf.")