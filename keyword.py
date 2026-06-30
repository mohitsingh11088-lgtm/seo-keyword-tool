import requests

# -----------------------------
# Google Suggestions
# -----------------------------
def get_google_suggestions(keyword, country="in"):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={keyword}&gl={country}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    try:
        return response.json()[1]
    except:
        return []


# -----------------------------
# YouTube Suggestions
# -----------------------------
def get_youtube_suggestions(keyword, country="in"):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={keyword}&gl={country}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    try:
        return response.json()[1]
    except:
        return []


# -----------------------------
# Main Program
# -----------------------------
seed = input("Enter seed keyword: ")
country = input("Enter country code (us/uk/in/ca/au): ").lower()

keywords = set()

# Step 1: base suggestions
base_google = get_google_suggestions(seed, country)
base_youtube = get_youtube_suggestions(seed, country)

keywords.update(base_google)
keywords.update(base_youtube)

# Step 2: expand keywords (second level)
for kw in list(keywords):
    more_google = get_google_suggestions(kw, country)
    keywords.update(more_google)

# Step 3: clean & output
keywords = sorted(list(keywords))

print(f"\nTotal Keywords Found: {len(keywords)}")
print(f"Country: {country.upper()}\n")

for k in keywords:
    print("-", k)