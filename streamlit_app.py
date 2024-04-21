import streamlit as st
import plotly.express as px

# Page functions
def page_home():
    st.title("Welcome Home!")
    st.write("This is the home page. Feel free to explore the other pages.")

def page_about():
    st.title("About This App")
    st.write("This app demonstrates multi-page navigation using buttons in Streamlit.")

def page_data():
    st.title("Data Visualization")
    df = px.data.iris()  # Load sample Iris dataset
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    st.plotly_chart(fig)

def page_contact():
    st.title("Contact Us")
    st.write("Reach out to us at: example@example.com")

# Dictionary of pages
pages = {
    "Home": page_home,
    "About": page_about,
    "Data": page_data,
    "Contact": page_contact
}

# --- Styling ---
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            padding-top: 2rem;
            padding-bottom: 10rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .stTabs > div[role="tablist"] > .stTab {
            flex: 1;
        }
        .stTabs > div[role="tablist"] {
            display: flex;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Layout ---
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", list(pages.keys()))

with st.container():  # Create a container for content
    st.title("My Streamlit App")
    st.write("Explore different functionalities using the navigation menu.")

    # Display the selected page
    pages[selected_page]()
