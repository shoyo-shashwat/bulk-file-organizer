# Bulk File Organizer

A powerful Python CLI utility to intelligently organize files in any directory by their type.

## Features

- Scans directories and organizes files by type
- Customizable organization rules via YAML config
- Dry-run mode to preview changes
- Comprehensive logging of all operations
- Error handling for file conflicts

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/bulk-file-organizer.git
cd bulk-file-organizer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python organiser.py /path/to/directory --dry-run
python organiser.py /path/to/directory
```

## Configuration

Edit `config.yaml` to customize file categories and extensions.