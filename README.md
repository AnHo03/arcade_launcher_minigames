# Arcade Game Suite

A modular Python project featuring two interactive command-line games:
- **Rock, Paper, Jenah** – a moral choice-driven twist on the classic game
- **Guess My Number** – a randomized number guessing challenge with performance tracking

This project serves as a demonstration of core Python development skills including class-based design, control flow, localization support, stat tracking, and modular architecture.

---

## Games Overview

### 🧠 Rock, Paper, Jenah (`RPS.py`)
A multilingual, expanded version of Rock-Paper-Scissors with layered logic and user-driven outcomes.

**Key Features:**
- Implements game logic using Python’s `Enum`
- Tracks game progress and user metrics (win/loss, tie, cheating, happiness, morality)
- Dual-language support via dictionary-based localization (`MESSAGES`)
- Nested function structure for game flow control
- Uses conditionals to implement moral consequence branching

**Skills Demonstrated:**
- Enum-based decision handling
- Input validation and error management
- State tracking with scoped nonlocal variables
- Dynamic message formatting and dictionary-based localization
- Custom control flow for replay, exit conditions, and progression checkpoints

---

### 🔢 Guess My Number (`guess_number.py`)
A randomized number guessing game with persistent statistics and a replay loop.

**Key Features:**
- User selects a number (1–5) and competes against a randomized computer choice
- Tracks performance metrics and calculates win percentage
- Nested logic and input sanitization for repeated gameplay

**Skills Demonstrated:**
- Use of `random.choice()` for basic randomization
- Loop structures and user prompt control
- Floating-point arithmetic for dynamic percentages
- Recursion for input validation and replay
- `sys.exit()` for controlled termination outside the loop

---

## Execution

Launch the program from terminal:

```bash
python arcade.py
```

You’ll be prompted to:
- Choose a game
- Enter player name
- Select a language (English or Spanish for Rock, Paper, Jenah)

---

## File Structure

```
arcade/
├── arcade.py            # Entry script and menu logic
├── RPS.py               # Rock, Paper, Jenah implementation
├── guess_number.py      # Guessing game logic
└── README.md            # Project documentation
```

---

## Requirements

- Python 3.7+
- No external libraries required

---

## Author

Developed by Andrew, a senior Biology and Geology student at UH–Clear Lake.  
This project merges programming with interactive design and demonstrates practical coding in a modular format.
