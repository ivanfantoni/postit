# **Post-it** v1.0.0
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## A simple CLI application for notes.

Allows you to:
- Add a new note
- Delete a note
- Change the priority of a note
- Edit the text of a note

## Usage
`postit [-h] [-i] [-d DELETE] [-e EDIT] [-p {normal, medium, hight}] [-t]`

## Options

- `-i`, `--insert`: Insert a new Post-it note.
- `-d`, `--delete`: Delete a Post-it note by its ID.
- `-e`, `--edit`: Select a Post-it note ID to edit.
- `-p`, `--priority`: Assign priority to the Post-it note. (Choose from: normal, medium, hight) (use with -e).
- `-t`, `--text`: Edit the text of a Post-it note by its ID (use with -e).

## License

This application is licensed under the MIT License.
