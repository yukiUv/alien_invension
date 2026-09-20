# Alien Invasion

A 2D arcade-style space shooter developed using **Python and Pygame**.

This project was built to develop practical experience with **Python, Object-Oriented Programming, event-driven programming, game-loop architecture, collision detection, state management, and modular software design**.

---

## Project Overview

**Alien Invasion** is a classic arcade-style game where the player controls a spaceship and defends against an incoming fleet of aliens.

The player can move the spaceship horizontally, fire bullets, destroy aliens, earn points, and progress through increasingly difficult levels.

The project is structured as a **modular, object-oriented, event-driven application**, making the code easier to understand, maintain, debug, and extend.

---

## Features

* Player-controlled spaceship
* Dynamic alien fleet generation
* Projectile firing and management
* Bullet–alien collision detection
* Alien fleet movement
* Player lives system
* Score tracking
* High-score tracking
* Progressive difficulty
* Level progression
* Play and restart functionality
* Real-time scoreboard
* Sound effects
* Custom game assets
* Centralized game configuration
* Game-state management

---

### Project Architecture

The project follows a **modular, object-oriented, event-driven architecture** centered around a continuous game loop.

### Game Flow

```text
Game Initialization
        ↓
Event Handling
        ↓
Game State Update
        ↓
Collision Detection
        ↓
Object Movement
        ↓
Rendering
        ↓
Repeat Game Loop
```

### Directory Structure

```text
alien_invasion/
│
├── alien_invasion.py      # Application entry point and main game loop
├── settings.py            # Centralized game configuration
├── game_functions.py      # Core gameplay and event-handling functions
├── game_stats.py          # Game state and runtime statistics
├── ship.py                # Player spaceship class
├── alien.py               # Alien class
├── bullet.py              # Projectile class
├── button.py              # Play button and UI interaction
├── scoreboard.py          # Score and game-status display
│
├── images/                # Game images and sprites
│   └── ...
│
├── sounds/                # Sound effects
│   └── ...
│
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignored files
```

---

## Core Components

### `alien_invasion.py`

The main entry point of the application.

Responsible for:

* Initializing Pygame
* Creating the game window
* Creating game objects
* Starting the main game loop
* Controlling the overall execution flow

---

### `settings.py`

Contains centralized configuration values such as:

* Screen dimensions
* Background settings
* Ship speed
* Alien speed
* Bullet speed
* Bullet limits
* Scoring values
* Difficulty scaling

Centralizing these values makes the game easier to configure and balance.

---

### `game_functions.py`

Contains the main gameplay and utility functions.

Responsibilities include:

* Keyboard and mouse event handling
* Ship movement
* Bullet firing
* Bullet updates
* Alien movement
* Fleet creation
* Collision detection
* Level progression
* Game-state transitions
* Removing inactive game objects

---

### `game_stats.py`

Maintains runtime game statistics and state information.

Examples include:

```text
Score
High Score
Current Level
Remaining Ships
Game Active State
```

---

### `ship.py`

Defines the player spaceship as an object.

Responsible for:

* Ship position
* Horizontal movement
* Screen boundary restrictions
* Ship rendering
* Ship reset/positioning

---

### `alien.py`

Defines alien objects and their behavior.

Responsible for:

* Alien position
* Alien movement
* Alien direction
* Alien rendering
* Fleet movement behavior

---

### `bullet.py`

Defines projectile objects.

Responsible for:

* Bullet position
* Bullet movement
* Bullet rendering
* Projectile lifecycle

---

### `scoreboard.py`

Responsible for displaying game information to the player.

Displays:

* Current score
* High score
* Current level
* Remaining ships

---

### `button.py`

Provides the interactive **Play** button used to start or restart the game.

---

## 🛠️ Technologies Used

| Technology                   | Purpose                                     |
| ---------------------------- | ------------------------------------------- |
| **Python 3**                 | Core programming language                   |
| **Pygame 2.6.1**             | Game framework and multimedia functionality |
| **OOP**                      | Modeling game entities and behavior         |
| **Event-Driven Programming** | Keyboard and mouse input                    |
| **Game Loop Architecture**   | Real-time game execution                    |
| **Collision Detection**      | Object interaction                          |
| **Git**                      | Version control                             |
| **GitHub**                   | Source-code hosting                         |
| **Visual Studio Code**       | Development environment                     |
| **Python ****`venv`**        | Dependency isolation                        |

---

## Gameplay

The player controls the spaceship using the keyboard.

### Controls

| Key     | Action      |
| ------- | ----------- |
| `←`     | Move left   |
| `→`     | Move right  |
| `Space` | Fire bullet |
| `Q`     | Quit game   |

> Controls may vary depending on the current implementation.

---

## Difficulty System

The game becomes progressively more challenging as the player advances.

Difficulty can increase through parameters such as:

```python
speedup_scale = 1.1
score_scale = 1.5
```

These values allow gameplay speed and scoring to scale as the player progresses through levels.

---

## Scoring System

Players receive points for destroying aliens.

The game maintains:

* Current score
* High score
* Level-based progression

The scoreboard provides real-time feedback during gameplay.

---

## Audio

The project includes audio assets to provide gameplay feedback and improve the overall game experience.

Audio resources are organized separately from the Python source code.

```text
sounds/
├── ...
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/alien-invasion.git
```

### 2. Navigate to the Project

```bash
cd alien-invasion
```

### 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows Command Prompt:

```cmd
venv\Scripts\activate
```

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not included, install Pygame directly:

```bash
pip install pygame
```

### 6. Run the Game

```bash
python alien_invasion.py
```

---

## Requirements

The project was developed using:

```text
Python 3
Pygame 2.6.1
```

You can create a dependency file with:

```bash
pip freeze > requirements.txt
```

---

## Screenshots

### Main Gameplay

*Add your gameplay screenshot here.*

```markdown
![Alien Invasion Gameplay](images/gameplay.png)
```

### Higher-Level Gameplay

<img width="1492" height="941" alt="image" src="https://github.com/user-attachments/assets/f390262e-f61b-47ed-9d67-8c7d78faafc8" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/19ee043a-b796-4a7b-947a-93e611c4b433" />


### Project Architecture
Project Architecture

Alien Invasion follows a modular, object-oriented, event-driven architecture built around a continuous Pygame game loop. 
Each module has a focused responsibility,
separating game configuration, state management, gameplay logic, entities, and presentation.

<img width="1176" height="957" alt="image" src="https://github.com/user-attachments/assets/0ddb6735-16b2-4c10-b381-db2cf4dbe842" />

Module Responsibilities
Module	Responsibility
alien_invasion.py	Initializes the application and controls the main game loop
settings.py	Stores centralized configuration and gameplay parameters
game_functions.py	Handles input, gameplay operations, collisions, fleet management, and state transitions
game_stats.py	Maintains runtime state such as score, level, high score, and remaining ships
ship.py	Defines the player spaceship and its movement behavior
alien.py	Defines alien entities and fleet movement behavior
bullet.py	Defines projectile behavior and lifecycle
button.py	Implements the interactive Play button
scoreboard.py	Renders score, high score, level, and player status
images/	Contains graphical resources
sounds/	Contains audio resources
Game Execution Flow

Each frame follows the general execution cycle:

1. Process Pygame Events
          ↓
2. Update Game State
          ↓
3. Move Ship / Bullets / Aliens
          ↓
4. Detect Collisions
          ↓
5. Update Score / Lives / Level
          ↓
6. Render Game Objects
          ↓
7. Display Updated Frame
          ↓
8. Repeat
Design Principles

The architecture applies several fundamental software development principles:

Separation of Concerns — Configuration, state, entities, gameplay logic, and UI are separated into dedicated modules.
Encapsulation — Game entities manage their own state and behavior through classes.
Modularity — Individual components can be modified or extended independently.
Single Responsibility — Modules are organized around specific responsibilities.
Centralized Configuration — Gameplay parameters are maintained in settings.py.
Event-Driven Execution — User input is processed through Pygame's event system.
State-Based Gameplay — Player lives, score, level, and active game state are maintained separately from rendering logic.

This architecture provides a clean foundation for extending the project with additional enemies, weapons, power-ups, levels, menus, and other gameplay systems.

## 🧠 Learning Outcomes

This project helped me gain practical experience with:

* Python programming
* Object-Oriented Programming
* Classes and objects
* Modular application design
* Event-driven programming
* Game-loop architecture
* Collision detection
* State management
* File and resource management
* Debugging
* Software architecture
* Version control with Git
* Project documentation

More importantly, it helped me understand how individual programming concepts can be combined to create a complete software application.

---

## 🚀 Future Improvements

Potential future improvements include:

* [ ] Additional enemy types
* [ ] Boss battles
* [ ] Power-ups
* [ ] Multiple weapons
* [ ] Background music
* [ ] More advanced animations
* [ ] Additional levels
* [ ] Difficulty selection
* [ ] Pause functionality
* [ ] Settings menu
* [ ] Save/load game progress
* [ ] Improved graphics
* [ ] Windows installer
* [ ] Expanded test coverage

---

## 📚 Inspiration

This project was inspired by the **Alien Invasion** project from:

> *Python Crash Course* by Eric Matthes

The implementation was developed and extended as a practical programming project to improve my understanding of Python and software development.

---

## 👨‍💻 Developer

**Chandima Udugama Withanage**

Undergraduate Student – Bachelor of Information Technology (Honors)

Interested in:

* Software Development
* Python
* Artificial Intelligence
* Machine Learning
* DevOps
* Technology

---

## 📄 License

This project is intended primarily for educational and portfolio purposes.

If you reuse or modify this project, please provide appropriate attribution.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

**Thank you for checking out Alien Invasion! 🚀👽**
