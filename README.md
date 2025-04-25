# pytest-api

(Below steps are based on WinOs)

## 1. Install Node.js, Java, Python.

## 2. Install pip packages for your project.

```commandline
pip install -r requirements.txt
```

## 3. Run your automation script, like:

```commandline
python runner.py - run

python runner.py - generate_report

python runner.py - open_report

python runner.py - generate_report - open_report

python runner.py - run - generate_report - open_report

python runner.py - run --keyword=test_delete

python runner.py - run --mark=P0

python runner.py - run --keyword=test_delete --mark=sanity

python runner.py - run --case_files=tests\feature_a\test_postman_demo.py

python runner.py - run --last_failed=True

python runner.py - run --concurrency=2

python runner.py - run --maxfail=2

python runner.py - run --failed_first

python runner.py - run --ignore=tests\feature_a\test_postman_demo.py

```