import whois  # Library for retrieving WHOIS domain registration information
import tldextract  # Extracts domain and subdomain from a URL
import re  # Regular expressions for text processing
from datetime import datetime  # Used for calculating domain age
import requests  # HTTP requests to get hosting and IP info

# Author: Wilson Marin
# Date: 2/19/2025
# Block 2 - CS3090

def checkWhois(domain):
    """
    Retrieves and analyzes WHOIS information of a given domain.
    - Checks the domain's registration date and warns if it's less than a year old.
    - Retrieves registrar information.
    - Cleans and analyzes domain status codes for potential risks.
    """
    try:
        w = whois.whois(domain)  # Fetch WHOIS data

        # Some WHOIS servers return a list of creation dates; take the first one
        if isinstance(w.creation_date, list):
            creation_date = w.creation_date[0]
        else:
            creation_date = w.creation_date

        # Calculate domain age and warn if it's less than a year old
        if creation_date:
            domain_age_days = (datetime.now() - creation_date).days if creation_date else None
            print(f"📅 Domain was registered on: {creation_date}")

            if domain_age_days and domain_age_days < 365:
                print("⚠️ Warning: This domain is less than a year old, it may be a phishing site!")
        else:
            print("⚠️ Warning: Could not determine domain registration date.")

        # Print registrar information if available
        if w.registrar:
            print(f"🏛️ Registrar: {w.registrar}")
        else:
            print("⚠️ Warning: Registrar information is missing.")

        # Analyze domain status for security flags
        if w.status:
            # Remove extra text and URLs from status codes for readability
            clean_statuses = [re.sub(r"\s*\(.*?\)|\s*https?://\S+", "", s) for s in w.status]
            print("🔍 Cleaned Domain Status:", clean_statuses)

            # Check if the domain lacks standard security protections
            if "clientTransferProhibited" not in clean_statuses:
                print("⚠️ Warning: This domain may not have standard security protections!")
    
    except Exception as e:
        print("❌ Error retrieving WHOIS information:", str(e))


def detect_homograph(domain):
    """
    Detects potential homograph attacks by checking for common character substitutions.
    - Looks for characters that resemble others (e.g., '0' for 'o', '1' for 'l').
    - Warns if the domain contains suspicious characters.
    """
    suspicious_chars = {'0': 'o', '1': 'l', '5': 's', '8': 'B', '4': 'A'}  # Common homograph substitutions
    detected = any(char in domain for char in suspicious_chars.keys())  # Check if domain has these characters

    if detected:
        print("⚠️ Potential homograph attack detected in domain name!")
    else:
        print("✅ No homograph attack detected.")


def get_hosting_info(domain):
    """
    Retrieves hosting and IP information of a domain using ipinfo.io.
    - Returns the country and organization hosting the domain.
    """
    try:
        response = requests.get(f"https://ipinfo.io/{domain}/json")  # Query IP info API
        data = response.json()  # Parse JSON response
        print(f"🌍 {domain} is hosted in {data.get('country', 'Unknown')} ({data.get('org', 'Unknown')})")
    except Exception as e:
        print("❌ Error retrieving hosting information:", str(e))


def main():
    """
    Main function that:
    - Takes user input (a URL).
    - Extracts the main domain name.
    - Runs WHOIS checks, homograph detection, and hosting info retrieval.
    """
    url = input("🔗 Enter a URL: ")  # Get URL from user input
    extracted = tldextract.extract(url)  # Extract domain components
    domain = f"{extracted.domain}.{extracted.suffix}"  # Format domain name (e.g., example.com)

    print(f"\n🔍 Checking domain: {domain}\n")

    checkWhois(domain)  # Run WHOIS analysis
    detect_homograph(domain)  # Check for homograph attacks
    get_hosting_info(domain)  # Get hosting information


# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
