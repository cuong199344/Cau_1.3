import streamlit as st

st.title('Random Words Generator')
st.header('Random Words')
st.header('&mdash;')
st.write('Meaning: &mdash;')
st.markdown('''
Click the :gray-background[:green[generate]] button to generate new word
''')
st.button('Generate')
