import streamlit as st

def Chucking(text):
    if text:
        # Splits the string into a list of words using spaces
        chunks = text.split()
        
        # Displaying the total count is helpful for the user to see!
        st.write("Total Words Extracted:", len(chunks))

        # CRITICAL ADDITION: Return the list of chunks to the main file
        return chunks
    return []