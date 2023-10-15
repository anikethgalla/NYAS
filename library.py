import streamlit as st
from googlesearch import search

def search_book(book_name):
    query = f"{book_name} book"
    num_results = 10  # You can adjust the number of search results to fetch

    try:
        search_results = list(search(query, num_results=num_results))
        
        if not search_results:
            st.error(f"No results found for '{book_name}' book.")
        else:
            st.success(f"Found {len(search_results)} results for '{book_name}' book:")
            for i, result in enumerate(search_results, start=1):
                st.write(f"Result {i}: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Resources")
    book_name = st.text_input("Enter the name of the book:")
    if st.button("Search"):
        search_book(book_name)

if __name__ == "__main__":
    main()