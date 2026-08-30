import streamlit as st 
import warnings
from PIL import Image


warnings.filterwarnings('ignore')
def jogar(palavra_secreta, palavra=[]):
  for letra in palavra_secreta:
    palavra.append(' __ ')
  st.header(palavra)
  st.session_state.palavra_secreta = palavra_secreta
  st.session_state.palavra = palavra
  st.write("A palavra secreta tem " + str(len(palavra_secreta)) + " letras")
  st.session_state.erro = 0


def chute(letra='', acerto=""):
 
  acerto = acerto.upper()
  palavra_secreta = st.session_state.palavra_secreta
  palavra = st.session_state.palavra
  chute = letra
  
  

  if acerto == palavra_secreta:
    st.header('vc acertou a palavra... parabens!!!!')
    st.header(f'A PALAVRA SECRETA É: {palavra_secreta}') 
    st.balloons() 
  
  elif acerto != '' and palavra_secreta:
    try:
      imagem = Image.open("imagens/total.PNG")
      st.image(imagem)
      st.header("VOCÊ PERDEU!!!!!")
      st.header(f'A PALAVRA SECRETA É: {palavra_secreta}')  
    except FileNotFoundError:
      st.error("Imagem não encontrada. Verifique o caminho!")
     
 
  if chute in palavra_secreta:       
    for index, letra in enumerate(palavra_secreta):
      if (chute == letra):
       palavra[index] = letra
       st.header(palavra)  
       st.success("vc acertou a letra")      
       st.balloons()
       if palavra == palavra_secreta:
         print(palavra_secreta,palavra)
         st.header('CAMPEAO')
  else:
    st.write("vc errou a letra")  
    st.session_state.erro +=1
    if st.session_state.erro == 1:
      try:
        imagem3=Image.open("imagens/cabeca.PNG")
        st.image(imagem3)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
    if st.session_state.erro == 2:
      try:
        imagem4=Image.open("imagens/mao_dir.PNG")
        st.image(imagem4)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
    if st.session_state.erro == 3:
      try:
        imagem5=Image.open("imagens/mao_esq.PNG")
        st.image(imagem5)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
        
    if st.session_state.erro == 4:
      try:
        imagem6= Image.open("imagens/corpo.PNG")
        st.image(imagem6)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
      
    if st.session_state.erro == 5:
      try:
        imagem7=Image.open("imagens/pe_dir.PNG")
        st.image(imagem7)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")

    if st.session_state.erro == 6:
      try:
        imagem8= Image.open("imagens/total.PNG")
        st.image(imagem8)
        st.header("VOCÊ PERDEU!!!!!")
        st.header(f'A PALAVRA SECRETA É: {palavra_secreta}')
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
      


st.set_page_config(page_title="Jogo da Forca", layout="wide")
try:
  imagem2 = Image.open("imagens/boneco.PNG")
  st.image(imagem2, width=200)
  st.audio("audio/musica.mp3", autoplay=True)
except FileNotFoundError:
  st.error("Imagem não encontrada. Verifique o caminho!")
st.markdown(
      "<h1 style='text-align: center;'>JOGO DA FORCA</h1>",
      unsafe_allow_html=True,)  
coluna1,coluna2,coluna3 = st.columns((3))



with coluna2:  
  st.subheader("Digite a palavra secreta")
  palavra_secreta = st.text_input("Digite a palavra secreta", type="password").upper()
  iniciar = st.button("Iniciar o jogo")
  if iniciar:
    jogar(palavra_secreta)



  st.subheader("Chute!!!!!")
  acerto=st.text_input('A palavra secreta e...')
  letra = st.text_input("Digite uma letra: ", max_chars=1).upper()
  if st.button("Chutar"):    
    chute(letra,acerto)
  
     
    
