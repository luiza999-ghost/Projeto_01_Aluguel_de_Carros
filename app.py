import streamlit as st
st.title("fofinho s motorcycle store") 
st.subheader('só veiculos grandes👌')
st.sidebar.title('escolha um modelo')
st.sidebar.image('logo.png')
carros=['catepilar', 'mercedes', 'scania', 'volvo']
opção=st.sidebar.selectbox('escolha o carro que foi alugado',carros)
st.image(f"{opção}.png")
st.markdown(f"##voce alugou om modelo:{opção}")
st.markdown('---')