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
    st.balloons() 
  
  if acerto != '' and palavra_secreta:
    try:
      imagem = Image.open("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/total.PNG")
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
        imagem3=Image.open("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/cabeca.PNG")
        st.image(imagem3)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
    if st.session_state.erro == 2:
      try:
        imagem4=Image.open("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/mao_dir.PNG")
        st.image(imagem4)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
    if st.session_state.erro == 3:
      try:
        imagem5=Image.open("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/mao_esq.PNG")
        st.image(imagem5)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
        
    if st.session_state.erro == 4:
      try:
        imagem6= Image.open("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/corpo.PNG")
        st.image(imagem6)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
      
    if st.session_state.erro == 5:
      try:
        imagem7=Image.open("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/pe_dir.PNG")
        st.image(imagem7)
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")

    if st.session_state.erro == 6:
      try:
        imagem8= Image.open("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/total.PNG")
        st.image(imagem8)
        st.header("VOCÊ PERDEU!!!!!")
        st.header(f'A PALAVRA SECRETA É: {palavra_secreta}')
      except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho!")
      


st.set_page_config(page_title="Jogo da Forca", layout="wide")
st.markdown(
      "<h1 style='text-align: center;'>JOGO DA FORCA</h1>",
      unsafe_allow_html=True,)
coluna1,coluna2,coluna3 = st.columns((3))
try:
  imagem2 = Image.open("https://www.google.com/search?sca_esv=2a75c7f50559d645&sxsrf=APpeQntjgUniKSHQgHVtBQBsh-qvWpB1EQ:1788083809413&udm=2&fbs=ABfTbFVGaQeaqnsRPI5sOMG32KszkLt6nAp8aiRKj5vMjqZApKUKSutr57PWW9cO7WMBPoU5S3sCPG7Bibu4itHJxOrLaUZ3dPts0zGHy4eIzbD3oeAbtieAys2V_3DVz52KhWXf0irYH4JnuWsZJWBOJwcidG0ThW8zpJpdE5SMZY8QFv3CtkE4V8fjPs8SyMLx-duxORXdPEJ3zjqs90pHpipGMuZ5tg&q=forca&sa=X&ved=2ahUKEwjgmqeii8iWAxV9ALkGHTz6KWsQtKgLegQIFhAB&biw=1366&bih=641&dpr=1#sv=CAMSXhoyKhBlLUthZ3FrSU03a1VvUVNNMg5LYWdxa0lNN2tVb1FTTToOR3V6VVpEMlp4V2szZU0gBCokCg5KWWpHRHN3OW16UzFqTRIQZS1LYWdxa0lNN2tVb1FTTRgAMAEYByDFk4fJBUoIEAEYASABKAE")
  st.image(imagem2, width=200)
  st.audio("audio/musica.mp3", autoplay=True)
  
except FileNotFoundError:
  st.error("Imagem não encontrada. Verifique o caminho!")


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
  
     
    
