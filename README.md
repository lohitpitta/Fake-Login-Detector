# Fake web Page Detector

LIVE AT :
https://fake-login-detector-wbq1.onrender.com

wait for a few seconds, after clicking this link..

## Description
This is a Flask-based phishing detection tool that analyzes URLs and identifies potentially suspicious login pages.

## Features
- Detects HTTP URLs
- Detects suspicious keywords:
  - login
  - secure
  - verify
- Displays Safe or Suspicious result

## Technologies Used
- Python
- Flask
- HTML
- CSS

## How to Run

1. Install Flask

```bash
python -m pip install flask
```

2. Run the application

```bash
python app.py
```

3. Open browser

```text
http://127.0.0.1:5000
```

## Example

Input:

```text
https://insta-login-secure.xyz
```

Output:

```text
⚠️ Suspicious URL
```

## Author
LOHIT
