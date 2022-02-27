# Semgrep automated script

## Step 1: Install semgrep

```bash
pip install semgrep
```

## Step 2: Add semgrep to PATH

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Step 3: Run script

```bash
$ python semgrep.py -h
usage: semgrep.py [-h] -z ZIPFILE

optional arguments:
  -h, --help            show this help message and exit
  -z ZIPFILE, --zipfile ZIPFILE
                        Project's ZIP file
```

```bash
$ python semgrep.py -z ~/sample-project/akamon-csharp.zip
```

You can config URL or path to ruleset by modifying CONFIG variable in app.py
