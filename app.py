from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    status = None
    
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        
        # First check if it's a valid URL format
        if not is_valid_url(url):
            result = "Invalid URL format"
            status = "warning"
        else:
            url_lower = url.lower()
            
            # Check for suspicious patterns
            suspicious_keywords = ['login', 'secure', 'verify']
            is_http = url_lower.startswith('http://')
            has_suspicious_keyword = any(keyword in url_lower for keyword in suspicious_keywords)
            
            if is_http or has_suspicious_keyword:
                result = "Suspicious URL"
                status = "danger"
            else:
                result = "Safe URL"
                status = "safe"
    
    return render_template('index.html', result=result, status=status)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
