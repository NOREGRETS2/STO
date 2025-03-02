from tkinter import filedialog
import shutil
from docx import Document
import docx



name_and_path_file = ""
with open('inside/end.txt', 'w') as f:
    f.write(name_and_path_file)

def trim_path(full_path):
    # Разделение пути по символу '/'
    parts = full_path.split('/')
    # Выбираем последний элемент списка (имя файла)
    file_name = parts[-1]
    return file_name

# Функция для сохранения результатов проверки
def copy_docx(original_file_name, output_file_name):
    # Копирование содержимого исходного документа в новый документ отчета
    shutil.copy2(original_file_name, output_file_name)

def coment_all(file_name, errors):
    doc = Document(file_name)
    for i in range(len(errors[0])):
        for paragraph in doc.paragraphs:
            if errors[1][i] in paragraph.text:
                if errors[0][i] not in [comment.text for comment in paragraph.comments]:
                    paragraph.add_comment(errors[0][i])
                break
    doc.save(file_name)

#Функция которая откроет нам файл и положит его имя и путь в переменную
def open_file_func():
    name_and_path_file = filedialog.askopenfilename()
    if name_and_path_file != "":
        with open('inside/end.txt','w') as f:
            f.write(name_and_path_file)
        text_path_file.config(text="Выбранный файл: " + name_and_path_file + ", отчёт сохранен в папку с программой")
        import processing_CFG_in_txt, E_check, a_check, k_check, m_check

        a_errors = a_check.errors
        k_error = k_check.massiv_k
        m_error = m_check.m_errors

        error_1_e = E_check.error416
        error_2_e = E_check.error31

        e_error = [[], []]

        e_error[1].append(a_errors[1][3])
        e_error[1].append(a_errors[1][3])

        e_error[0].append(error_1_e)
        e_error[0].append(error_2_e)

        trimmed_original_filename = trim_path(name_and_path_file)
        filename_copy = "Отчёт " + trimmed_original_filename
        copy_docx(name_and_path_file, filename_copy)

        coment_all(filename_copy, k_error)
        coment_all(filename_copy, a_errors)
        coment_all(filename_copy, e_error)
        coment_all(filename_copy, m_error)

    else:
        text_path_file.config(text="Файл не выбран либо выбран не правильно")
        with open('inside/end.txt','w') as f:
            f.write(name_and_path_file)


