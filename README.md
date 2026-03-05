# Alien Invasion

This project processes data about "alien ships" positions from text files and calculates their precise coordinates based on given dimensions and scaling factors. It features an interactive console interface for easily selecting input data files and generating corresponding output files.

## Project Structure

```text
alien_invasion/
│
├── inputs/           # Directory for input text files to be processed (e.g., `alien.in`).
├── outputs/          # Directory where generated results are saved (e.g., `alien.out`).
├── src/              # Folder for source code.
│   ├── main.py       # Main entry point providing the interactive CLI menu.
│   ├── solution.py   # Core business logic processing the text grid and calculating coordinates.
│   └── utils.py      # Helper utilities for file input/output and reading directory contents.
└── README.md         # General documentation and instructions.
```

## How the Code Works

1. **`src/main.py`**: Runs an interactive command-line loop, presenting all files found in the `inputs/` directory. The user selects an input file by typing its corresponding list number.
2. **`src/utils.py`**: Provides utilities to read the content of the selected input file as a string, write text to the output file, and iterate the `inputs` folder to present the CLI menu options.
3. **`src/solution.py`**: 
   - Receives the raw string content of an input file and reads the number of test cases.
   - For each test case, it parses grid dimensions ($x$, $y$) and a scaling factor ($z$).
   - Scans an $x \times y$ textual grid to group "ships" mapped by alphabetical characters (e.g., `A`, `b`, etc.).
   - Computes the bounding box minimums and maximums (`[x1, y1, x2, y2]`) for each ship, identifying its geometric center.
   - Orders the ships by their total grid area in ascending order.
   - Multiplies each ship's center coordinates by the factor $z$, rounds to 3 decimal places, and formats the output data.

## How to Run the Script

1. Ensure you have Python installed (Python 3.x).
2. Open a terminal or command prompt.
3. Navigate to the project's root directory:
   ```bash
   cd path/to/alien_invasion
   ```
4. Run the main script via Python:
   ```bash
   python src/main.py
   ```
5. Follow the interactive menu on the screen. Type the number of the input file you want to process (for example, type `1` and press Enter to select `alien.in`). Type `0` and press Enter to exit the program.
6. Check the `outputs/` folder. A new file with the `.out` extension (e.g., `alien.out`) will be created containing the calculated output format.