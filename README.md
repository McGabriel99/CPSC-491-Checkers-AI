# CPSC-481-Checkers-AI

## Problem Statement

This project focuses on the development of an enhanced Checkers game, utilizing Python and Pygame for graphical display and AI algorithms for gameplay logic.

## Files and Directories

`gui.py`: Main graphical user interface file that uses Pygame to render the game board and handle user interactions. It defines functions for drawing the board, pieces, handling mouse inputs, and updating the game state.

`images/`: Contains graphical assets used in the game. For example:

- `crown.png`: Image used to denote king pieces on the board.

`pvp/`: **Player vs. Player mode**

- `pvp_checkers_helper.py`: Contains the game logic for handling player versus player interactions, including board setup, move validation, and game rules specific to PvP scenarios.

- `pvp_gui.py`: GUI setup for the PvP version of the game, handling rendering and player input specifically for games involving two human players.


`pvsai/`: **Player vs. AI mode**

- `checkers_helper.py`: Similar to pvp_checkers_helper.py but includes additional logic for AI behaviors.

- `gui.py`: GUI setup for playing against the AI, including mechanisms for AI move generation and execution.

`simple_checkers.py`: A simplified version of the Checkers game aimed at beginners, with minimalistic UI and basic game functionalities. Useful for understanding the core concepts without the complexities of the full GUI or AI components.

## Installation

**Python**: Main programming language used for all game logic and graphical interfaces.

**Pygame**: Library used for creating the graphical user interface and handling user interaction.

**Random**: Python standard library used for generating pseudo-random numbers for AI decision-making processes.

## How to run

**Player vs. Player mode**

1. `cd pvp/`

2. `python pvp_gui.py`

3. Click to play

**Player vs. AI mode**

1. `cd pvsai/`

2. `python gui.py`

3. Click to play

**Console Mode**

1. `python simple_checkers.py`

2. Follow instructions on terminal

## Future Work
Further enhancements could include improving AI decision-making algorithms, introducing networked multiplayer capabilities, and expanding the graphical user interface to support more interactive elements and animations.
