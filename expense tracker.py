import streamlit as st
st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("😎Personal Expense Tracker")
# ---------------- SESSION STATE ---------------- #
if "expenses" not in st.session_state:
    st.session_state.expenses = []
# ---------------- LAYOUT ---------------- #
col1, col2 = st.columns(2)
# ---------------- FORM ---------------- #
with col1:
    st.subheader("➕ Add Expense")
    with st.form("expense_form"):
        title = st.text_input("Expense Title")
        amount = st.number_input("Amount", min_value=0.01, step=0.01)
        category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills"])
        add = st.form_submit_button("Add Expense")
        if add:
            if title.strip() == "":
                st.error("Please enter a valid expense title.")
            elif amount <= 0:
                st.error("Please enter a valid amount greater than 0.")
            else:
                st.session_state.expenses.append({
                    "title": title,
                    "amount": amount,
                    "category": category
                })
                st.success("Expense Added!")
                st.rerun()  # Clear the form by rerunning the app
# ---------------- DISPLAY ---------------- #
with col2:
    st.subheader("📊 Expense Summary")
    if st.session_state.expenses:
        total = sum(item["amount"] for item in st.session_state.expenses)
        st.write(f"💷   Total Expense: ₹{total}")
        # Interactivity: Toggle
        show_details = st.toggle("Show Detailed Expenses")
        if show_details:
            for i, item in enumerate(st.session_state.expenses):
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    st.write(f"{item['title']} - ₹{item['amount']} ({item['category']})")
                with col_b:
                    if st.button("Delete", key=f"delete_{i}"):
                        st.session_state.expenses.pop(i)
                        st.rerun()
        # Interactivity: Filter
        category_filter = st.selectbox("Filter by Category",
                                      ["All", "Food", "Travel", "Shopping", "Bills"])
        if category_filter != "All":
            filtered = [e for e in st.session_state.expenses if e["category"] == category_filter]
            filtered_total = sum(item["amount"] for item in filtered)
            st.write(f"Filtered Total for {category_filter}: ₹{filtered_total}")
            st.write("Filtered Results:")
            for item in filtered:
                st.write(f"{item['title']} - ₹{item['amount']}")
    else:
        st.warning("No expenses added yet!")                      