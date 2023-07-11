import streamlit as st


st.title("Z OR T DECISION")

with st.form("z_or_t", clear_on_submit=True):
    sigma = st.radio("Does it have Sigma ? ", ("Yes", "No"))
    normal = st.radio("Is it Normal?", ("Yes", "No"))
    n = st.radio("n>=30?", ("Yes", "No"))

    submitted = st.form_submit_button("CHECK")

    if submitted:
        if sigma == "Yes":
            if normal == "Yes":
                st.write("USE Z DISTRIBUTION")
            else:
                if n == "Yes":
                    st.write("USE Z DISTRIBUTION")
                else:
                    st.write("DONT USE ANY")
        else:
            if normal == "Yes":
                st.write("USE T DISTRIBUTION")
            else:
                if n == "Yes":
                    st.write("USE T DISTRIBUTION")
                else:
                    st.write("DONT USE ANY")
