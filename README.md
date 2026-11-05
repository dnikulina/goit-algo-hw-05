# Python Functional Programming & Error Handling

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Generators](https://img.shields.io/badge/Python-Generators-green?style=flat-square)
![Decorators](https://img.shields.io/badge/Python-Decorators-purple?style=flat-square)
![Regex](https://img.shields.io/badge/Regex-Text%20Processing-lightgrey?style=flat-square)

## Overview

This repository contains four Python exercises focused on closures, recursion, generators, regular expressions, log processing, decorators, and exception handling.

## Tech Stack

- Python
- Regular expressions
- Generators
- Closures
- Recursion
- Decorators
- File I/O
- Command Line Interface

## Tasks

### 1. Cached Fibonacci

[task_one.py](./task_one.py)

Implements a closure-based Fibonacci calculator with memoization.

The function stores previously calculated values in a cache to avoid repeated recursive calculations.

### 2. Number Generator & Profit Calculation

[task_two.py](./task_two.py)

Uses a generator and regular expression to:

- extract floating-point numbers from text;
- yield values one by one;
- calculate their total sum through a separate function.

### 3. Log File Analyzer

[task_three.py](./task_three.py)

Implements a command-line log analysis tool that:

- parses log lines into structured dictionaries;
- counts entries by log level;
- displays summary statistics;
- optionally filters and displays logs for a selected level.

### 4. Contact Assistant with Error Handling

[task_four.py](./task_four.py)

Extends a basic CLI contact manager with a decorator that handles common input errors such as:

- missing arguments;
- invalid values;
- unknown contacts.

## Learning Outcomes

This homework helped me practice:

- closures and nested functions;
- recursion and caching;
- generators and lazy iteration;
- regex-based text extraction;
- higher-order functions;
- decorators;
- exception handling;
- command-line data processing.
