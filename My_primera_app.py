import streamlit as st

ja

def main():
    st.title("Mi primera app")
    st.write("Autor: Esta app fue elaborada por Jean Carlos Perilla")

    user_name = st.text_input("Ingresa tu nombre", "Escribe aquí...")

    if user_name:
        st.write(f"{user_name}, te doy la bienvenida a mi primera app.")

if __name__ == "__main__":
    main()

