import streamlit as st
import requests

BACKEND_URL = "http://localhost:8080" # Replace with the actual address

def fetch_units():
    response = requests.get(f"{BACKEND_URL}/units")
    st.write(f"response status code:{response.status_code}")
    st.write(f"response json:{response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch units from the backend")
        return []

def create_unit(name):
    response = requests.post(f"{BACKEND_URL}/units", json={"name": name})
    if response.status_code == 200:
        st.success("Unit created successfully")
        return response.json()
    else:
       st.error("Failed to create a unit, try again.")
       return None

def owner_dashboard():
    st.title("Owner Dashboard")
    st.write(f"Welcome, {st.session_state['username']}!")
    
    # Sidebar navigation for admin dashboard
    with st.sidebar:
        st.subheader("Admin Navigation")
        if st.button("Unit Management"):
            st.session_state["admin_view"] = "unit_management"
        if st.button("Payment Tracking"):
            st.session_state["admin_view"] = "payment_tracking"
        if st.button("Bulletin Board"):
            st.session_state["admin_view"] = "bulletin_board"
        if st.button("Maintenance Reports"):
            st.session_state["admin_view"] = "maintenance_reports"

    # Display the current admin view
    if st.session_state["admin_view"] == "unit_management":
        st.header("Unit Management")
        st.write("Current Units:")
        units = fetch_units()
        if units:
            st.table(units)

        st.subheader("Add New Unit")
        with st.form("add_unit_form"):
            new_unit_name = st.text_input("Unit Name")
            submitted = st.form_submit_button("Add Unit")
            if submitted:
                create_unit(new_unit_name)
                st.experimental_rerun()
    elif st.session_state["admin_view"] == "payment_tracking":
        st.header("Payment Tracking")
        st.write("This is where you will track payments.")
    elif st.session_state["admin_view"] == "bulletin_board":
        st.header("Bulletin Board")
        st.write("This is where you will post announcements.")
    elif st.session_state["admin_view"] == "maintenance_reports":
        st.header("Maintenance Reports")
        st.write("This is where you will view maintenance reports.")

    if st.button("Logout"):
        st.session_state["view"] = "login"