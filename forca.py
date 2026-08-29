import streamlit as st 
import warnings


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
    st.image("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/total.PNG")
    st.header("VOCÊ PERDEU!!!!!")
    st.header(f'A PALAVRA SECRETA É: {palavra_secreta}')   
 
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
      st.image("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/cabeca.PNG")
    if st.session_state.erro == 2:
      st.image("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/mao_dir.PNG")
    if st.session_state.erro == 3:
      st.image("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/mao_esq.PNG")
    if st.session_state.erro == 4:
      st.image("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/corpo.PNG")
    if st.session_state.erro == 5:
      st.image("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/pe_dir.PNG")
    if st.session_state.erro == 6:
      st.image("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/total.PNG")
      st.header("VOCÊ PERDEU!!!!!")
      st.header(f'A PALAVRA SECRETA É: {palavra_secreta}')


st.set_page_config(page_title="Jogo da Forca", layout="wide")
st.markdown(
      "<h1 style='text-align: center;'>JOGO DA FORCA</h1>",
      unsafe_allow_html=True,)

#st.image("https://github.com/maxrangel01/forca-com-streamlit/blob/main/imagens/boneco.PNG", width=200)
st.audio(https://github.com/maxrangel01/forca-com-streamlit/blob/main/audio/musica.mp3, autoplay=True)
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
  
     
    
