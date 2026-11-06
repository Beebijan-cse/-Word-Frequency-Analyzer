# Word Frequency Analyzer

A command-line tool that reads a text file, counts how often each word appears, and generates a report of the most common words.

## Features

- Reads plain text files and handles missing files gracefully
- Cleans text by lowercasing it and removing punctuation
- Ignores common stop words such as "the", "and", and "is"
- Shows the top N most frequent words with a text bar chart
- Reports total words, unique words, and the most common word
- Saves the report to a `.txt` file

## Skills Demonstrated

- String processing and cleaning
- Dictionaries for counting
- Sorting and ranking results
- File reading and writing
- Error handling with `try`/`except`

## Requirements

- Python 3.6 or later
- No external dependencies

## Installation

```bash
git clone https://github.com/Beebijan-cse/-Word-Frequency-Analyzer.git
cd -Word-Frequency-Analyzer
```

## Usage

```bash
python word_frequency.py
```

Enter the path to a text file when prompted, then choose how many top words to display. The report is printed to the screen and saved to a `.txt` file.

## Example

```
Top 5 words:
the       ******** (8)
data      ***** (5)
...

Total words: 120
Unique words: 58
Most common word: the
```

## Project Structure

```
-Word-Frequency-Analyzer/
├── word_frequency.py
├── sample.txt
├── README.md
└── .gitignore
```

## Possible Improvements

- Allow custom stop word lists
- Export results to CSV
- Add unit tests

## Author

Beebijan A · [GitHub](https://github.com/Beebijan-cse) · [LinkedIn](https://www.linkedin.com/in/a-beebijan-76703b42a)
