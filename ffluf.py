import subprocess

# Fuzz Fast w/ Love Uew Fool - v gpt0.0.1#
# (Fast Fuzzing with Love and Unexpected Friendliness)#

# Get the target URL and wordlist from the user
target_url = input("Enter the target URL: ")  # "http://example.com/FUZZ"
wordlist_file = input("Enter the wordlist file: ")  # "all.lst"

# Set the valid response codes
valid_codes = "200,204,301,302,307,401,403"

# Read the wordlist from the file
try:
    with open(wordlist_file, 'r', encoding='utf-8-sig') as f:
        words = f.read().splitlines()
except UnicodeDecodeError:
    with open(wordlist_file, 'r', encoding='ISO-8859-1') as f:
        words = f.read().splitlines()

# Fuzz the target URL with each word in the wordlist
results = []
for word in words:
    url = target_url.replace("FUZZ", word)
    cmd = f"ffuf -u {url} --input-cmd 'cat {wordlist_file}' -fw {valid_codes}"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode("utf-8").strip()
    if output:
        results.append((url, output))

# Print the results
for result in results:
    print(result)
