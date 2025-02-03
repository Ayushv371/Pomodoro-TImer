# Pomodoro Timer

A simple Pomodoro Timer application built using Python and Tkinter. This app helps you stay productive by implementing the Pomodoro Technique, alternating between focused work sessions and short breaks.

## Features
- **Work & Break Cycles**: 25-minute work sessions followed by short breaks.
- **Long Breaks**: Every four cycles, a long break is provided.
- **Visual Timer**: Displays countdown and updates dynamically.
- **Session Tracking**: Uses checkmarks to track completed work sessions.
- **Reset Functionality**: Easily reset the timer when needed.

## Requirements
Ensure you have the following installed:
- Python 3.x
- `tkinter` (comes with Python by default)

## How to Use
1. Run the script:
   ```sh
   python pomodoro_timer.py
   ```
2. Click "Start" to begin the Pomodoro cycle.
3. Work during the session, and take breaks when prompted.
4. Click "Reset" to stop and reset the timer.

## File Structure
- `pomodoro_timer.py` - The main script for the application.
- `tomato.png` - Image used for visual representation.

## How It Works
- **25-minute work sessions** followed by **5-minute short breaks**.
- After **4 work sessions**, a **20-minute long break** is triggered.
- The app visually tracks progress with checkmarks.


