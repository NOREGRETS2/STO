# Файл CFG оформляется исключительно по пунктам начинающимися с порядкового номера и кончающегося _run БЕЗ пробелов и кончающегося _end при этом пустых строк БЫТЬ НЕ ДОЛЖНО!
#файл CFG
file_cfg = "inside/CFG.txt"
file_key = "inside/end.txt"

#разбиение построчно в массив с названием
def read_cfg_to_array(file_cfg):
    with open(file_cfg, 'r') as file:
        lines_cfg = file.readlines()
    return lines_cfg

#колхоз с получением полного пути файла
def get_name_and_path(file_key):
    with open(file_key,'r') as f:
        name_and_path_file = f.read()
    return name_and_path_file

#сканим любой параметр
def extract_paranetr(array_cfg_massiv, start_element, end_element):
    start = array_cfg_massiv.index(start_element)
    end = array_cfg_massiv.index(end_element)
    return array_cfg_massiv[start+1:end]

array_cfg_massiv = read_cfg_to_array(file_cfg)

#Тут задаем свою выгрузку
name_and_path_file = get_name_and_path(file_key)

array_parametr_filename = extract_paranetr(array_cfg_massiv, '1_filename_run\n', 'filename_end\n')

array_alexandr = extract_paranetr(array_cfg_massiv,'3_alex_run\n','alex_end\n')
array_maxim = extract_paranetr(array_cfg_massiv,'5_maxim_run\n','maxim_end\n')
array_andrey = extract_paranetr(array_cfg_massiv,'2_andray_run\n','andray_end\n')
array_kostya = extract_paranetr(array_cfg_massiv,'4_kostya_run\n','kostya_end\n')



