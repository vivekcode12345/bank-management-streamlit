import streamlit as st
from main import Bank

bank = Bank()

st.title("🏦 Simple Bank Application")

menu = st.sidebar.selectbox(
    "Menu",
    ["Create Account", "Deposit", "Withdraw", "Show Details", "Delete Account"]
)

if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):
        success, msg = bank.create_account(name, age, email, int(pin))
        if success:
            st.success(f"Account created! Account No: {msg}")
        else:
            st.error(msg)

elif menu == "Deposit":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = bank.deposit(acc, int(pin), amt)
        st.success(msg) if success else st.error(msg)

elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = bank.withdraw(acc, int(pin), amt)
        st.success(msg) if success else st.error(msg)

elif menu == "Show Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = bank.get_user(acc, int(pin))
        if user:
            st.json(user)
        else:
            st.error("Invalid credentials")

elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = bank.delete_account(acc, int(pin))
        st.success(msg) if success else st.error(msg)
