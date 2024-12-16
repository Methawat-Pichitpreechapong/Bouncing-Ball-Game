# Bouncing_Ball_Game
This game is **"Bounce Master"**. It's a dynamic arcade-style game where players control a paddle to bounce a ball, break bricks, and navigate challenging levels featuring obstructions, all while competing for high scores.

**Description**
"Bounce Master" is an interactive arcade-style game that challenges players to control a paddle, bounce a ball, and strategically break bricks across multiple levels. The game introduces dynamic obstacles and varying difficulty, making it a fun and skill-testing experience. It combines elements of physics-based simulation for realistic ball dynamics and obstruction interactions, with engaging visuals and mechanics to deliver a classic yet modern gaming experience.

**Feature**

1. **Multiple Difficulty Levels:**
   - Three levels of difficulty (Easy, Medium, Hard), each offering unique challenges such as varying paddle sizes, ball speeds, and brick arrangements.

2. **Dynamic Obstacles:**
   - Levels 2 and 3 introduce obstructions that the ball interacts with, adding an extra layer of complexity and requiring strategic gameplay.

3. **Customizable Experience:**
   - Players can enter their name at the start, which is displayed alongside their current score, adding a personalized touch to the game.

4. **Realistic Ball Physics:**
   - The game uses physics-based mechanics for the ball’s interactions with bricks, the paddle, walls, and obstructions, ensuring an engaging and authentic experience.

5. **Score Tracking and Reset:**
   - The game keeps track of the player’s score, which resets when restarting the game in the same level or returning to the menu.

6. **Visual Feedback:**
   - A vibrant design with dynamic color schemes for bricks, ball, and obstructions, making the game visually appealing.

7. **Game Over and Victory Messages:**
   - Players receive a clear indication of success or failure with customized "YOU WON" or "GAME OVER" messages.

8. **Simple Controls:**
   - Intuitive controls (arrow keys for paddle movement, Escape to return to menu) ensure accessibility for players of all skill levels.

**Installation and Running Guide for "Bounce Master"**

1. **Prerequisites:**
   - Ensure you have Python installed on your system (version 3.7 or later is recommended).
   - Install the `tkinter` library if it's not pre-installed (usually included with Python).

2. **Installation Steps:**
   - **Option 1:** Download the source code file (`bounce_master.py`) from the provided repository or location.
   - **Option 2:** Copy and paste the source code into a new Python file using any text editor (e.g., VS Code, PyCharm, or IDLE). Save the file as `bounce_master.py`.

3. **Running the Project:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the `bounce_master.py` file is saved.
   - Run the script using the following command:
     ```
     python bounce_master.py
     ```
   - The game window will appear, and you can start playing by entering your name and selecting a difficulty level.

**Usage**
   - This is the link i provided for you 
    "video link"

**Purpose of each class**
   - `Ball` class : Represents the ball in the game. It handles the movement of the ball and interactions (collisions) with other game objects like the paddle, bricks, walls, and obstructions.
   - `Paddle` class : Represents the player's paddle. It moves horizontally and is controlled by keyboard input.
   - `Bricks` class : Represents individual bricks that the ball can hit and destroy. Each brick is drawn on the canvas and removed upon collision with the ball.
   - `Game` class : the central controller of the game. It manages the state of the game, initializes objects like the ball, paddle, bricks, and obstructions, and handles user input and scoring.










