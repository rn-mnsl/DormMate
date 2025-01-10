import streamlit as st
from admin_dashboard import owner_dashboard

# Initialize session state variables
if "view" not in st.session_state:
    st.session_state["view"] = "login"  # Default view is the login page
if "user_type" not in st.session_state:
    st.session_state["user_type"] = None
if "username" not in st.session_state:
    st.session_state["username"] = None

# Sidebar for login buttons
st.sidebar.title("DormMate")
if st.sidebar.button("User Login"):
    st.session_state["user_type"] = "Tenant"
    st.session_state["view"] = "login_form"

if st.sidebar.button("Admin Login"):
    st.session_state["user_type"] = "Dorm Owner"
    st.session_state["view"] = "login_form"


# Login Form UI and Logic
def login_form():
    st.subheader("Sign in")
    username = st.text_input("Username, Email, or Phone number")
    password = st.text_input("Password", type="password")
    if st.button("Sign in"):
        st.session_state["username"] = username
        if st.session_state["user_type"] == "Tenant":
            st.session_state["view"] = "tenant_dashboard"
        else:
            st.session_state["view"] = "owner_dashboard"

# Tenant dashboard UI
def tenant_dashboard():
    st.title("Tenant Dashboard")
    st.write(f"Welcome, {st.session_state['username']}!")
    st.write("This is the tenant dashboard.")
    if st.button("Logout"):
        st.session_state["view"] = "login"


# Main application logic (view controller)
if st.session_state["view"] == "login":
    st.title("Welcome to DormMate!")
elif st.session_state["view"] == "login_form":
    login_form()
elif st.session_state["view"] == "tenant_dashboard":
    tenant_dashboard()
elif st.session_state["view"] == "owner_dashboard":
    owner_dashboard()