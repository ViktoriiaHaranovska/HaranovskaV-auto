Overview:

Welcome to the project! This repository aims to provide a framework, developed by Haranovska Viktoriia, for showcasing automated testing of API, UI, and Database functionalities. The project is particularly valuable as it demonstrates automation solutions for testing popular websites such as GitHub and Chess.com.

Getting Started:

To get started with the project, it is recommended to begin exploring the config folder. The config.py file is utilized to verify whether the program functions as expected. 

Proceed to the modules folder, where you will find classes such as:

GitHub: This class contains various methods for retrieving information from the GitHub API.
Database: Represents an object for interacting with the database (become_qa_auto.db in the root folder) and includes methods for performing various data operations.
ChessDotComAutomation: Contains preparatory methods for automating user actions on the chess.com website.


tests Folder:
Houses tests for the aforementioned methods.
API tests for GitHub, including checks for user existence, repository existence, finding a repository with a single-character name, and locating a comment by its number.
Database tests for data retrieval, updates, column addition and removal, column count, and response speed verification.
UI tests for GitHub and Chess.com, covering scenarios like login with incorrect credentials, changing the theme on Chess.com, starting a new game with a random opponent, and surrendering in a game.
