# 🎮 Tic-Tac-Toe Game with Minimax AI

A terminal-based **Tic-Tac-Toe game** implemented in **Python**, supporting both **single-player** (vs computer) and **multiplayer** modes. The single-player mode features an **AI opponent powered by the Minimax algorithm**, ensuring optimal moves and making it unbeatable.

---

## 🧠 Key Features

- 🔁 **Two Game Modes**  
  - Single Player (Human vs AI)  
  - Multiplayer (Human vs Human)

- 🤖 **AI with Minimax Algorithm**  
  - Ensures the computer always makes the best move  
  - Recursively evaluates board states for optimal strategy

- 🧩 **Game Mechanics**  
  - Real-time game board rendering in the terminal  
  - Input validation and error handling  
  - Clean and interactive command-line interface

---

## 🧩 Core Components

- `minmax(board, Player)`: Implements the recursive Minimax logic to evaluate and select optimal moves.  
- `Compturn()`: Computer’s move logic using the Minimax algorithm.  
- `User1turn()` & `User2turn()`: Handle player moves with input and validation.  
- `ConstBoard()`: Renders the game board in a readable 3x3 layout.  
- `anlyzeboard()`: Checks the board for win conditions or a draw.

---

## 🛠 Technologies Used

- **Language:** Python  
- **Concepts:**  
  - Recursion  
  - Minimax Algorithm  
  - CLI (Command Line Interface)  
  - Game Logic  
  - Decision Trees

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
