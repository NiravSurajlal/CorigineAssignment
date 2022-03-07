# CorigineAssignment
## Description
This program takes a single integer argument and computes its factorial. It then computes the sum of the digits of the factorial, finally providing this as an output.

This program was designed using _python3_ and includes the _sys_ library. It was developed to run in a Docker container.

## Files
    1. main.py      - python file containing the code
    2. Dockerfile   - creates Docker container

## Example Usage
For a given positive integer **N**, the code calculates N! and then the sum of that answer. The results are displayed in the command line. 
    $ docker run --rm factorial-digits 10
    27
    $ docker run --rm factorial-digits 100
    648

## Installation
