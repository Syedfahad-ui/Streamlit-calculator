import streamlit as st
import math

st.set_page_config(page_title="Python Web Calculator", page_icon="🧮")

st.title("🧮 Python Web Calculator")

# --- Input field ---
expression = st.text_input("Enter your expression", "")

col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate"):
        try:
            result = eval(expression)
            st.success(f"Result: {result}")
        except ZeroDivisionError:
            st.error("❌ Cannot divide by zero!")
        except Exception:
            st.error("❌ Invalid Expression!")

with col2:
    if st.button("Clear"):
        st.experimental_rerun()

# --- Extra buttons ---
st.markdown("### 🔢 Quick Functions")

col3, col4, col5 = st.columns(3)

with col3:
    if st.button("√ Square Root"):
        try:
            result = math.sqrt(float(expression))
            st.success(f"Result: {result}")
        except:
            st.error("❌ Error in square root calculation")

with col4:
    if st.button("x² (Square)"):
        try:
            result = float(expression) ** 2
            st.success(f"Result: {result}")
        except:
            st.error("❌ Error in square calculation")

with col5:
    if st.button("% Percentage"):
        try:
            result = float(expression) / 100
            st.success(f"Result: {result}")
        except:
            st.error("❌ Error in percentage calculation")

st.markdown("---")
st.markdown("Made by *Syed Fahad Ehsan*")