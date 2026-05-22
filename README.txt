# Sociolinguistic Style Profiler

A Python-based sociolinguistic analysis tool that detects stylistic markers and classifies language register using a rule-based profiling system and SQLite database.

## Project Description

This project analyzes sociolinguistic features in user-written text.

The program detects markers associated with:

- internet slang
- casual speech
- Gen Z speech
- formal register
- academic register
- politeness strategies
- hedging and uncertainty

The system uses a custom SQLite dictionary containing weighted sociolinguistic markers.

## Features

- SQLite-based sociolinguistic dictionary
- 60+ linguistic markers
- Register classification
- Weighted feature scoring
- Style profiling
- Marker explanations
- Interactive terminal interface

## Example Input

```text
bro ngl this essay was kinda fire but maybe the argument needs more evidence
```

## Example Output

```text
Overall style: Gen Z / online youth style

Detected markers:
- bro
- ngl
- kinda
- fire
- maybe
- evidence
```

## Technologies Used

- Python
- SQLite
- Rule-based NLP methods
- Sociolinguistic feature analysis

## How to Run

```bash
python3 main.py
```

## Future Improvements

- GUI interface
- Visualization dashboard
- Larger sociolinguistic dictionary
- Multi-word expression detection
- Corpus statistics
- CSV export