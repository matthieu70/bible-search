import streamlit as st
import json
import re

st.set_page_config(page_title="📖 جستجوی کتاب مقدس", layout="wide")

@st.cache_data
def load_bible():
    with open("bible.json", "r", encoding="utf-8") as f:
        return json.load(f)

bible_data = load_bible()

def search_bible(search_term):
    results = []
    count = 0
    search_pattern = re.compile(re.escape(search_term), re.IGNORECASE)

    for book, chapters in bible_data["کتاب مقدس"].items():
        for chapter, verses in chapters.items():
            for verse_num, verse_text in verses.items():
                if search_pattern.search(verse_text):
                    results.append((book, chapter, verse_num, verse_text))
                    count += verse_text.lower().count(search_term.lower())

    return results, count

st.title("📖 جستجوی کتاب مقدس")
st.markdown("### سازنده: **محسن ضعیف‌نژاد**")

search_term = st.text_input("🔍 واژه موردنظر را جستجو کنید:")

if search_term:
    results, count = search_bible(search_term)
    st.markdown(f"✅ تعداد تکرار واژه **{search_term}** در کل کتاب مقدس: **{count}** بار")
    
    if results:
        st.markdown("### 📌 نتایج جستجو:")
        for book, chapter, verse_num, verse_text in results:
            st.markdown(f"📖 **{book} - فصل {chapter}، آیه {verse_num}**: {verse_text}")
    else:
        st.warning("❌ موردی یافت نشد.")