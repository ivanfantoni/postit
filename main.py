from post_it import Postit
from database import insert_postit, delete_postit, get_all_postits, edit_priority, edit_text
from colortext import Colortext
import argparse
import os

def insert():
    print('Enter/Paste new Post-it.\nCtrl-D to save it: ')
    content = []
    while True:
        try:
            line = input()
            content.append(line)
        except EOFError:
            insert_postit(Postit(text=('\n'.join(content))))
            get_all()
            break
        except KeyboardInterrupt:
            print(medium_priority('\n[ Exit ]\n'))
            break
    
def delete(id):
    delete_postit(id)
    get_all()

def get_all():
    postits = get_all_postits()
    os.system('clear')
    window_size = os.get_terminal_size().columns
    print(Colortext('*** Post-it ***').bold().light_yellow().run())
    print()
    postit_normal = []
    postit_medium = []
    postit_high = []
    for post in postits:
        line_txt = [line for line in post.text.split('\n')]
        line_txt = remove_empty_lines(line_txt)
        while line_txt != size_text(line_txt, window_size):
            line_txt = size_text(line_txt, window_size)

        lenght = [len(spl) for spl in line_txt]
        lenght.sort(reverse=True)
        lenght = lenght[0]

        prt_string = f' ID: {post.id} '
        if post.priority == 'normal' or post.priority == None:
            func = normal_priority 
            priority_list = postit_normal

        if post.priority == 'medium':
            func = medium_priority
            priority_list = postit_medium

        if post.priority == 'high':
            func = high_priority
            priority_list = postit_high

        upperline = func('┌' + prt_string + '─'*(lenght + 2 - len(prt_string)) + '┐')
        underline = func('└' + '─'*(lenght + 2) + '┘')

        if len(underline) < len(upperline):
            lenght = lenght + (len(upperline) - len(underline))
            upperline = func('┌' + prt_string + '─'*(lenght + 2 - len(prt_string)) + '┐')
            underline = func('└' + '─'*(lenght + 2) + '┘')  

        content = []
        for l in line_txt:
            line = func('│ ') + l + ' '*(lenght-len(l))+ func(' │\n')
            content.append(line)

        post_text = ''.join(content)
        content_text = f'{upperline}\n{post_text}{underline}'
        priority_list.append(content_text)

    for postit in postit_high+postit_medium+postit_normal:
        print(postit)

def e_priority(id, priority):
    edit_priority(id=id, priority=priority)
    get_all()

def e_text(id):
    text = input(f'Post-it {id} - Type new text: ')
    edit_text(id=id, text=text)
    get_all()

def remove_empty_lines(txt):
    while True:
        if txt[-1] == '' or txt[-1] == None:
            txt.pop(-1)
        else:
            break
    return txt

def size_text(lines, window_size):
    for i ,line in enumerate(lines):
        if len(line) + 4  > window_size - 4:
            cut_point = window_size - 4
            while line[cut_point] != ' ':
                cut_point -=1
            part1 = line[:cut_point+1]
            part2 = line[cut_point+1:]
            lines.pop(i)
            lines.insert(i, part1)
            lines.insert(i+1, part2)
    return lines

def normal_priority(txt):
    return Colortext(txt).bold().light_green().run()

def medium_priority(txt):
    return Colortext(txt).bold().light_yellow().run()

def high_priority(txt):
    return Colortext(txt).bold().light_red().run()

def main():
    id = None
    parser = argparse.ArgumentParser(prog='postit', description='Post-it v1.0.0. Fast CLI notes')
    parser.add_argument('-i', '--insert', help='Insert a new Post-it note', action='store_true')
    parser.add_argument('-d', '--delete', help='Delete a Post-it note by its ID', action='store')
    parser.add_argument('-e', '--edit', help='Select a Post-it note ID to edit', action='store')
    parser.add_argument('-p', '--priority', choices=['normal', 'medium', 'high'], 
                        help='Assign priority to the Post-it note by its ID (choose from: normal, medium, high) (use with -e)', 
                        action='store')
    parser.add_argument('-t', '--text', help='Edit the text of a Post-it note by its ID (use with -e)', action='store_true')

    args = parser.parse_args()

    if args.edit:
        id = args.edit

    if args.insert:
        insert()
    elif args.delete:
        delete(args.delete)
    elif args.priority:
        e_priority(id=id, priority=args.priority)
    elif args.text:
        e_text(id=id)
    else:
        get_all()

if __name__ == '__main__':
    main()









