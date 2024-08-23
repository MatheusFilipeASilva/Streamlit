import pandas as pd
import seaborn as sns
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from time import sleep

df = pd.read_csv(r"C:\Users\manoe\OneDrive\Documentos\Run_csv\input_M15_SINASC_RO_2019.csv")
st.sidebar.title('JORNADA STREAMLIT')
st.sidebar.header('O que é o streamlit?')
st.sidebar.header('Quais são suas principais funções?')
st.sidebar.header('Como o usuário pode interagir com os dados apresentados?')
st.sidebar.header('(HOJE, NO DEV REPORTER)')
st.header('Conhecendo o streamlit:')
st.markdown("""**O streamlit é uma biblioteca para desenvolvimento web,**
**voltado à ciência de dados! Ele se propõe a permitir a criação de um**
**ambiente interativo para exposição de dados, que possa ser operado por**
**usuários com pouca ou nenhuma experiência com front end**
**ele oferece diversas possibilidades, e estaremos apresentando algumas aqui!**
""")

st.markdown("""Os três tipos de texto apresentados anteriormente, são o title,
headder, e o markdown em negrito, respectivamente. O que estamos apresentando
agora, é o markdown comum.""")

st.markdown("""__Este trecho, por sua vez, foi escrito com markdown em itálico.
E poderiamos, com tranquilidade, combinar as duas coisas, assim:__""")
st.markdown("""__*NEGRITO E ITÁLICO*__""")

st.markdown("O streamlit também possui suporte para visualização de dataframes")
st.markdown('Observe:')
st.write(df)

df['PESO'] = df['PESO'].astype(str)
df['PESO'] = df['PESO'].str.replace(',', '.', regex=False)
df['PESO'] = df['PESO'].astype(float)


st.markdown("""O streamlit também suporta que o próprio usuário insira dados
            direto na página, que altere a visualização dos próprios conteúdos
            da mesma, por exemplo, delimitando valores que serão exibidos em
            um dataframe.""")


st.markdown("""Por exemplo, podemos estabelecer um limidador para quais]
            dados são exibidos em um Dataframe...""")

st.markdown("**Selecione abaixo os valores mínimos e máximo dos pesos das crianças que devem ser incluídas no dataframe!**")
st.markdown("**Selecione abaixo os valores mínimos e máximo dos pesos das crianças que devem ser incluídas no dataframe!**")
peso_min = st.slider('Peso Mínimo Incluído:', value=0, min_value=0, max_value=6000, step=1)
peso_max = st.slider('Peso Máximo Incluído:', value=peso_min, min_value=peso_min, max_value=6500, step=1)

st.markdown(f"**Segue abaixo as informações sobre as crianças que possuem peso (em gramas) entre {peso_min} e {peso_max}**")
df_selected = df[(df['PESO'] <= peso_max) & (df['PESO'] >= peso_min)]

st.write(df_selected)

st.markdown('''Uma outra excelente configuração do streamlit, é que ele permite, por exemplo, que o usuário escolha 
            parâmetros entre vários disponíveis. Veja:''')
st.markdown('**Escolha quais colunas abaixo você quer que estejam no DataFrame:**')

selected_columns = st.multiselect("Escolha quais colunas abaixo você quer que estejam no DataFrame:",
                                options=['PESO', 'IDADEMAE', 'ESCMAE', 'QTDFILVIVO', 'RACACOR'])

st.write(df_selected[selected_columns])

st.markdown('Podemos criar também barras de progresso, por exemplo:')

progress_bar = st.progress(0.0)

for i in range(100):
    sleep(0.001)
    progress_bar.progress(i+1)

st.markdown('Bem como caixas de seleção:')
st.selectbox(label='Selecione qual sua fruta favorita!', 
            options = ['UVA', 'MAÇÃ', 'JABUTICABA', 'BANANA', 'MORANGO'])

st.markdown('''Também é possível usar este recurso para passar parametros para
            a plotagem de um gráfico, por exemplo...''')

city_to_plot = st.selectbox(label='Selecione qual cidade irá ser plotado um gráfico dos APGAR5MEDIO X IDADEMAE!', 
            options = ["Alta Floresta D'Oeste", 'Alto Alegre dos Parecis', 'Ariquemes'])
df_city = df[df['munResNome'] == city_to_plot]

fig, ax = plt.subplots()

sns.barplot(x = 'munResNome', y = 'APGAR5', estimator = 'mean', data = df_city, ax = ax)
st.pyplot(fig)

st.markdown("""__*Nesta pequena jornada, exploramos algumas possibilidades de manipulação de dados interativa
            utilizando o streamlit. Vimos como utilizar negrito e itálico, títulos, barras laterais, barras de
            progresso, caixas de seleção, sliders, filtros em dataframe, entre outras coisas! O stramlit possibilita
            uma simples e forte interação entre usuário e base de dados que é de alto valor para um desenvolvedor
            que queira desenvolver relatórios e api's que realmente agregam valor para o seu trabalho de modelagem
            e extração de dados.*__""")