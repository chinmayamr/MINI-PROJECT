import streamlit as st

def find_largest(num1, num2, num3):
  largest = max(num1, num2, num3)
  return largest
st.title("Find the Largest Among 3 Numbers")
num1 = st.number_input("Enter Number 1:")
num2 = st.number_input("Enter Number 2:")
num3 = st.number_input("Enter Number 3:")
if st.button("Find Largest"):
  largest_number = find_largest(num1, num2, num3)
  st.write(f"The largest number is: {largest_number}")

