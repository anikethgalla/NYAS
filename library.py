import streamlit as st
import requests

def search_book(book_name):
    base_url = "http://openlibrary.org/search.json"
    params = {
        "title": book_name
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'docs' in data:
                books = data['docs']
                st.success(f"Found {len(books)} results for '{book_name}' book:")
                for i, book in enumerate(books, start=1):
                    title = book.get('title', 'Title not available')
                    author = book.get('author_name', ['Author not available'])[0]
                    cover = book.get('cover_i', '')
                    if cover:
                        cover_url = f"http://covers.openlibrary.org/b/id/{cover}-L.jpg"
                        st.image(cover_url, caption=f"Result {i}: Cover Image for '{title}'")
                    st.write(f"Result {i}: Title: {title}, Author: {author}")
                    st.write(f"Result {i}: Link: [Open Library Link](https://openlibrary.org/{book.get('key', '')})")
            else:
                st.error(f"No results found for '{book_name}' book.")
        else:
            st.error(f"Error fetching data from Open Library API.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Resources")
    book_name = st.text_input("Enter the name of the book:")
    if st.button("Search"):
        search_book(book_name)

if __name__ == "__main__":
    main()