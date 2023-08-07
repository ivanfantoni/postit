from post_it import Postit
from database import insert_postit, delete_postit, get_all_postits, edit_priority, edit_text
from colortext import Colortext
import argparse
import os

def insert():
    text = input('Insert new Post-It: ')
    insert_postit(Postit(text=text))
    get_all()

def delete(id):
    delete_postit(id)
    get_all()

def get_all():
    postits = get_all_postits()
    os.system('clear')
    print(Colortext('*** Post-it ***').bold().light_yellow().run())
    postit_normal = []
    postit_medium = []
    postit_high = []
    for post in postits:
        id = Colortext(post.id).bold().run()
        if post.priority == 'normal' or post.priority == None:
            prt = Colortext('*').bold().light_green().run()
            txt = Colortext('[ ').bold().light_green().run()+post.text+Colortext(' ]').bold().light_green().run()
            post_it = f'\n{prt} {id} {prt} {txt}\n'
            postit_normal.append(post_it)
        if post.priority == 'medium':
            prt = Colortext('*').bold().light_yellow().run()
            txt = Colortext('[ ').bold().light_yellow().run()+post.text+Colortext(' ]').bold().light_yellow().run()
            post_it = f'\n{prt} {id} {prt} {txt}\n'
            postit_medium.append(post_it)
        if post.priority == 'high':
            prt = Colortext('*').bold().light_red().run()
            txt = Colortext('[ ').bold().light_red().run()+post.text+Colortext(' ]').bold().light_red().run()
            post_it = f'\n{prt} {id} {prt} {txt}\n'
            postit_high.append(post_it)

    for postit in postit_high+postit_medium+postit_normal:
        print(postit)

def e_priority(id, priority):
    edit_priority(id=id, priority=priority)
    get_all()

def e_text(id):
    text = input(f'Post-it {id} - Type new text: ')
    edit_text(id=id, text=text)
    get_all()

def main():
    id = None
    parser = argparse.ArgumentParser(prog='postit', description='Post-it v1.0.0. Fast CLI notes')
    parser.add_argument('-i', '--insert', help='Insert a new Post-it note', action='store_true')
    parser.add_argument('-d', '--delete', help='Delete a Post-it note by its ID', action='store')
    parser.add_argument('-e', '--edit', help='Select a Post-it note ID to edit', action='store')
    parser.add_argument('-p', '--priority', choices=['normal', 'medium', 'high'], help='Assign priority to the Post-it note (choose from: normal, medium, high) (use with -e)', action='store')
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









