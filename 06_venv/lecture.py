# VIRTUAL ENV.
# 1. CREATE VENV.
### python3 -m venv venv
### source venv/bin/activate
### pip install requests
### pip freeze
# 2. SHARE CONFIGS (REQS.TXT)
### pip freeze > requirements.txt
# 3. RECREATE ENV.
### pip install -r . \requirements.txt

import requests

print('Hello, VENV world!')
