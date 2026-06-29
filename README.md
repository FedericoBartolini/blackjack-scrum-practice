# Blackjack Scrum Practice

This repository contains a simple text-based Blackjack game developed in Python.

The main aim of this project is to practise how Scrum can be used in a small group project. The focus is not on creating a perfect or advanced game, but on organising the work, dividing tasks, using Trello, and completing a short sprint as a team.

## Project goal

Build a basic text-based Blackjack game where the user plays against the computer.

The simplified rules are:

* The game uses a normal 52-card deck.
* Ace has value 1.
* J, Q, and K have value 10.
* The aim is to get as close as possible to 21 without going over.
* The user plays first.
* The computer draws cards until it reaches 18 or more.
* If a player goes over 21, they lose.
* If the user and computer have the same score, the computer wins.

## Codebase choice

The main codebase will use a normal Python file, for example `blackjack.py`.

This is the best option for the final game because the project is interactive and needs keyboard input. A `.py` file is also easier to run, share, and combine with code from different group members.

However, I recommend using Google Colab for quick testing of small functions, such as the deck, card values, or score calculation, before adding them to the main Python file.

## Role division

**Federico**
Scrum Master + Developer
Organise Trello, set sprint goal, keep deadline, create the Python game template, integrate code from other members, record decisions, and write sprint notes.

**@Samrawit Gebru**
Developer: Deck and cards
Create the 52-card deck, shuffle function, and card value system.

**@Tshilidzi Violet Masindi**
Developer: User input and output
Create the text display and `Y/N` input system.

**@Aida Hadi Rubio**
Product Owner / Client + Developer
Check that the rules are clear and help with game logic and winner rules.

## Simple sprint process

1. Agree on Blackjack and simplified rules.
2. Add the GitHub repo link in Trello Resources.
3. Put all task cards in Current Sprint.
4. Federico creates the Python template.
5. Each person completes their section of the code.
6. Combine all code into one Python file.
7. Test the game quickly.
8. Move finished cards to Done.
9. Write short sprint notes about what worked, what did not work, and what we would change next time.

## Trello task cards

The Trello board is used to organise the sprint.

Cards - Current Sprint:

* Sprint Goal
* Rules / Requirements
* Game Template
* Deck and Cards
* User Input
* Game Logic
* Computer Turn
* Testing
* Sprint Notes / Retrospective

Card - Resources:

* GitHub Repository

## Expected output

By the end of the sprint, the group should have:

* A simple Python Blackjack file.
* A Trello board showing the sprint progress.
* A short record of decisions and reflections.
* Notes about what worked well and what could be improved in the next sprint.
