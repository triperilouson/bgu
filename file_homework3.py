import pygame
import time
import sys
import time
import pygame
from pygame.locals import *
#try:
def students_check():
    bug = ' \n \t'
    student_assessment = []
    str_students = ''
    str_name = ''
    student_name = []
    with open('input.txt', 'r') as file:
        lines = file.read()
        print(lines)
    for line in lines:
        if line.isdigit():
            str_students += line
            if str_name != '':
                student_name.append(str_name)
                str_name = ''
        elif not line.isdigit():
            if str_students != '':
                student_assessment.append(int(str_students))
                str_students = ''
            elif line != ' ' and line != ',':
                str_name += line.strip()
    flag = 0

    if len(student_name) != len(student_assessment) and len(student_name) >= len(student_assessment):
        print('incorrect input: amount belong to name so big, please verify your file')
        flag = 1
    if len(student_name) != len(student_assessment) and len(student_name) <= len(student_assessment):
        print('incorrect input: amount belong to assessment so big, please verify your file')
        flag = 1

    if flag == 0:
        passing_grade = (sum(student_assessment))/len(student_name)
        with open('output.txt', 'w') as file_output:
            for i in range(len(student_assessment)):
                if student_assessment[i] >= passing_grade:
                    file_output.write(f"{student_name[i]}, {student_assessment[i]}")

    print(student_assessment)
    print(student_name)
#students_check()


def text_get_additional():
    #program_readout file and gives as to change it
    pygame.init()
    pygame.display.set_caption("События от клавиатуры")
    done = False
    screen = pygame.display.set_mode((900, 600))
    pygame.display.update()
    with open('output.txt', 'r') as file3:
        text = file3.read()
    print(text)
    while not done:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    done = True
                    break


                elif event.key == pygame.K_BACKSPACE:
                    with open('output.txt', 'r') as file3:
                        text = file3.read()
                        text = text[:-1]
                        time.sleep(1)
                    with open('output.txt', 'w') as file2:
                        file2.write(text)
                        time.sleep(1)
                    print(text)
                else:
                    text += event.unicode
                    time.sleep(1)
                    with open('output.txt', 'w') as file2:
                        file2.write(text)
                    with open('output.txt', 'r') as file3:
                        text = file3.read()
                        time.sleep(1)
                    print(text)

#text_get_additional()

def sorted_lines_in_files():
    with open("input1.txt", "r") as file1, open("input2.txt", "r") as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()


    combined_lines = sorted(lines1 + lines2)


    with open("output.txt", "w") as output_file:
        for line in combined_lines:
            output_file.write(line)
#sorted_lines_in_files()

def character_replacement():
    def read_file(file_path):
        """Читает строки из файла и возвращает список строк."""
        with open(file_path, 'r', encoding='utf8') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]

    def write_file(file_path, lines):
        """Записывает список строк в файл."""
        with open(file_path, 'w', encoding='utf8') as file:
            for line in lines:
                file.write(line + '\n')

    def remove_characters_and_reverse(lines, chars_to_remove):
        """Удаляет указанные символы с правого края строки, добавляет ';' и переворачивает строку."""
        chars_to_remove_set = set(chars_to_remove)  # Преобразуем в множество для быстрого поиска
        processed_lines = []
        for line in lines:
            # Удаляем символы с правого края строки
            while line and line[-1] in chars_to_remove_set:
                line = line[:-1]
            # Добавляем ';' и переворачиваем строку
            line = line + ';'
            reversed_line = line[::-1]
            processed_lines.append(reversed_line)
        return processed_lines

    def main():
        # Считываем строки из файла input.txt
        input_file_path = 'input.txt'
        lines = read_file(input_file_path)

        # Запрашиваем у пользователя набор символов для удаления
        chars_to_remove = input('Введите символы для удаления с правого края строки: ')

        # Обрабатываем строки
        processed_lines = remove_characters_and_reverse(lines, chars_to_remove)

        # Записываем перевернутые строки в файл output.txt
        output_file_path = 'output.txt'
        write_file(output_file_path, processed_lines)

        print(f'Обработанные строки записаны в файл {output_file_path}.')

    if __name__ == "__main__":
        main()
#character_replacement()
