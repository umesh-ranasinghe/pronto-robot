## Overview

This CLI application parses commands to control a robot and calculates the robot's distance from its starting point. The robot receives commands to move forwards or backwards, and turn left or right. Each command is in the format `<command><number>`, where `<command>` specifies the action and `<number>` specifies the magnitude.

For example, 'L1' means "turn left by 90 degrees once", and 'B2' means "go backward 2 units".

## Available Commands

- `F` - move forward 1 unit
- `B` - move backward 1 unit
- `R` - turn right 90 degrees
- `L` - turn left 90 degrees

## Task

Program receives a string of commands and outputs the robot's distance from its starting point. This distance is the minimum amount of units the robot needs to traverse to return to its starting point. It can move in the north, south, east, or west directions.

### Example

**Input:** `F1,R1,B2,L1,B3`  
**Output:** `4`

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the script.

## Usage

### Command Line Interface

To run the application from the command line, use the following command:

```bash
python robot.py "F1,R1,B2,L1,B3"
