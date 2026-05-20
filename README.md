# Python_programming-_internship3
# Personal Expense Tracker

A command-line financial tracking application written in Python. This tool helps users record daily financial transactions, categorize expenditures, and generate organized summaries to monitor spending habits over time.

Developed as part of the Python Programming Internship at SkillInfyTech Solutions.

## Features

- **Log Expenses**: Quickly record transaction data including the precise Amount spent, Category (e.g., Food, Travel, Bills), and a brief custom description.
- **Automated Timestamping**: Leverages system clocks to automatically stamp the exact date and time of each entry so users don't have to input it manually.
- **Persistent Data Storage**: Save all data into a local structured JSON file framework (`expenses.json`) to keep financial historical logs intact across program restarts.
- **Reporting & Summaries**: 
  - View a complete detailed ledger breakdown of all recorded historical logs with a running grand total calculation.
  - View real-time aggregated metrics grouped strictly by category to easily analyze where money is being allocated.

## Concepts & Skills Learned
- Working with JSON data encoding and decoding methods via Python's built-in `json` module.
- Utilizing structural data patterns (`lists` containing nested `dictionaries`).
- Date and time manipulation using the standard `datetime` library.
- Implementing control flow, simple data analytics tools, and safe console input parsing loops.

## Technical Requirements
- Python 3.x
- No external dependencies or external library setups required.

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/expense-tracker-cli.git](https://github.com/YOUR_USERNAME/expense-tracker-cli.git)
   cd expense-tracker-cli
