import streamlit as st
import requests

# -----------------------------
# Google Suggestions
# -----------------------------
def get_google_suggestions(keyword, country="in"):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={keyword}&gl={country}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        return requests.get(url, headers=headers, timeout=10).json()[1]
    except:
        return []


# -----------------------------
# YouTube Suggestions
# -----------------------------
def get_youtube_suggestions(keyword, country="in"):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={keyword}&gl={country}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        return requests.get(url, headers=headers, timeout=10).json()[1]
    except:
        return []


# -----------------------------
# UI START
# -----------------------------
st.title("🚀 SEO Keyword Research Tool")

seed = st.text_input("Enter seed keyword")
country = st.selectbox("Select country", ["us", "uk", "in", "ca", "au"])

if seed:

    keywords = set()

    # Step 1
    base_google = get_google_suggestions(seed, country)
    base_youtube = get_youtube_suggestions(seed, country)

    keywords.update(base_google)
    keywords.update(base_youtube)

    # Step 2 expand
    for kw in list(keywords)[:10]:
        more = get_google_suggestions(kw, country)
        keywords.update(more)

    keywords = sorted(list(keywords))

    st.subheader(f"Total Keywords Found: {len(keywords)}")

    for k in keywords:
        st.write("🔹", k)
