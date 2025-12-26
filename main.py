import streamlit as st
import time

st.set_page_config(page_title="Merry Christmas!", page_icon="❤️")

st.markdown("""
    <style>
    
    .stApp {
        background-color: #a30000;
        background-image: url("https://i.pinimg.com/736x/ba/b1/13/bab11318ee6b783d85530cc44c25f9e1.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    
    /* 2. Fix the top header strip to match */
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); /* Make it transparent */
    }
    
    /* 4. Text Styling */
    h1 {
        font-family: 'Caveat', cursive;
        font-size: 60px;
        color: #2c3e50;  /* Dark Blue/Grey Ink Color */
        text-shadow: 2px 2px 4px #00000020; /* Subtle ink bleed shadow */
        text-align: center;
    }
    h2, p {
        color: black !important;
        font-family: 'Courier New', monospace;
        text-shadow: 1px 1px 2px #00000020;
        text-align: center;
    }
    p {
        background-color: #bbd4b5;
        opacity: 0.9;
        padding: 10px;
        border-radius: 5px;
        display: block;

    }
    
    .stButton > button {
        background-image: url('https://png.pngtree.com/png-clipart/20250420/original/pngtree-classic-red-wax-seal-stamp-with-detailed-imprint-isolated-on-transparent-png-image_20744656.png');
        background-size: cover;
        background-position: center;
        background-color: transparent;
        border: none;
        height: 120px;  /* Adjust height */
        width: 120px;   /* Adjust width */
        position: fixed;
        bottom: 40px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 9999;
    }

    </style>
    """, unsafe_allow_html=True)


if 'closed' not in st.session_state:
    st.session_state.closed = True
    

st.title("To my Darling Lydia")

col_a, col_b, col_c = st.columns([1,1,1])
#with col_b:
    #st.image("https://cdn-icons-png.flaticon.com/512/3798/3798197.png", width=150)

col1, col2, col3 = st.columns([0.5, 2, 0.5])

#gift reveal
with col1:
    if not st.session_state.closed:
        st.write("""
        Thank you for always supporting and loving me, even on the worst days.
        You've always been there for me no matter what, you've given me a safe place to escape to when life is too much
        and your presence in my life has made me a better person. Being around you brings me a happiness I wasn't sure I'd
        get to experience again. You've ignited in me whimsy and joy that I thought I lost.
        You've made all my Christmas wishes come true nad more. I look forward to ever Christmas we get to spend together in the future.
        I want to make so many memories with you Lydia, I love you to the moon and back.
        
        With all my love,
        
        Jude
        """)
        
with col3:
    if st.session_state.closed:
        if st.button("", "Open Card"):
            st.session_state.closed = False
            st.rerun()
    else:
        if st.button("", "Close Card"):
            st.session_state.closed = True
            st.rerun()
        
