# **Phishing URL Detection Tool**

## Overview
This tool analyzes domain names to detect potential phishing attempts. It retrieves WHOIS information, checks for homograph attacks, and intendifies hosting details to helpusers assess whether a domain might be suspicious. 

## Features
- **WHOIS Lookup** – Retrieves domain registration details, including creation date, registrar, and status.  
- **Domain Age Check** – Warns if a domain is newly registered (less than a year old).  
- **Homograph Attack Detection** – Identifies potential phishing domains that use lookalike characters (e.g., `g00gle.com`).  
- **Hosting Information** – Retrieves the domain's hosting country and organization. 

## 🚀 Installation & Usage  

### Prerequisites  
Ensure you have **Python 3.x** installed. You will also need the following dependencies:  

```bash
pip install python-whois tldextract requests
```

### To run script on terminal:
python phishingDetector.py
Then enter the domain to be scanned and review potential wrning s or security concerns.

## Limitatins & Warnings
- This tool is for education and research purposes only.  It should not be relied upon for securing sensitive information.
- The detection methods do not guarantee absolute accuracy—a site flagged as "safe" may still be malicious. This tool only checks for basic safety measuremnts. 
- WHOIS data availability depends on registry policies; some domains may not provide full details.
- Homograph detection is basic and does not account for advanced Unicode-based attacks.
- The tool does not scan website content—it only analyzes domain characteristics.

### Ethical Considerations & Responsable Use
This tool is designed to help users understand domain security risks, but it must be used responsibly:

- Use it for learning, cybersecurity awareness, or personal safety.
- Do not use this tool for malicious purposes, such as attempting to identify targets for phishing.
- Do not assume absolute security based on results—always combine this with other security measures.
- Respect privacy laws—retrieving WHOIS data should be done within legal and ethical boundaries.

## License
This project is licensed under the MIT License.

### MIT License

Copyright (c) 2025 Wilsn Marin

Permission is hereby granted, free of charge, to any person obtaining a copy of this softwraae and associated document files (the "Software"), to deal in the Software without restriction including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
**The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.**

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.