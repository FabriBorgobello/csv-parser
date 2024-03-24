# CSV Parser

A Python script that processes CSV files and generates a report.

## Prerequisites

- [Python](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)

## Setup

1. Clone the repository

```bash
git clone https://yourprojectrepository.com
cd your-project-directory
```

2. Create and activate a virtual environment

```bash
# For Unix/macOS
python3 -m venv venv

# For Windows
python -m venv venv
```

```bash
# For Unix/macOS
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Add the CSV files

   Add the CSV files to the `data` directory (create it if it doesn't exist). Make sure the CSV files follow this naming convention: `YYYYMMDD_*.csv` (e.g. `20210101_Viajes_distritos.csv`).

## Usage

Run the script

```bash
python script.py
```
