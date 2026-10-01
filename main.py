

#pip install streamlit openai
import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key=st.secrets["GEMINI_API_KEY"],
                base_url='https://generativelanguage.googleapis.com/v1beta/openai')

#titulo
st.write('## ChatBot de IA')

#campo de mensagem (input)
if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []
    

mensagem_usuario = st.chat_input('escreva sua  mensagem aqui:')

for msg in st.session_state['lista_mensagens']:
    quem_enviou = msg['role']
    texto = msg['content']
    st.chat_message(quem_enviou).write(texto)

#quando o usuário enviar uma mensagem
    #mostrar a msg na conversa
if mensagem_usuario:
    st.chat_message('user').write(mensagem_usuario)
    msg1 = {'role': 'user',
            'content': mensagem_usuario}
    st.session_state['lista_mensagens'].append(msg1)

    #Mandar pra ia responder
    
    resposta = modelo.chat.completions.create(
        messages=st.session_state['lista_mensagens'],
        model='gemini-flash-lite-latest'

    )
    resposta_ia = resposta.choices[0].message.content

    #mostrar a resposta da AI
    st.chat_message('assistant').write(resposta_ia)
    msg2 = {'role': 'assistant',
            'content': resposta_ia}
    st.session_state['lista_mensagens'].append(msg2)

#manter o historico

#criar a IA
