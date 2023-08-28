import streamlit as st

def main():
    st.title("Mi primera app")
    st.write("Autor: Esta app fue elaborada por COLOQUE AQUÍ SU NOMBRE")

    user_name = st.text_input("Ingresa tu nombre", "Escribe aquí...")

    if user_name:
        st.write(f"{user_name}, te doy la bienvenida a mi primera app.")

if __name__ == "__main__":
    main()

