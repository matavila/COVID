import pandas as pd             #Análise de dados
import plotly.express as px     #Funciona para fazer os gráficos
import streamlit as st          #Funciona como se fosse o front-end



'''
    Uma vez que se tem um banco de dados no formato CSV, podemos então utiliza-lo através da biblioteca pandas
    Sendo assim iremos ler o dataset (Banco de dados) no github do wcota
'''
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

'''
    Como a tabela está em ingles iremos passar um código onde iremos melhorar a leitura dos dados pegando os nomes das colunas 
    do banco de dado e então passaremos os mesmo para portugues
'''
df = df.rename(columns={
    'newDeaths': 'Novos óbitos',
    'newCases': 'Novos casos',
    'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes'
    ,'totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'
    })

'''
    Nessa primeira parte do código, iremos fazer a seleção dos dados manualmente, sendo assim para que possamos criar uma lista com 
    os estados da pesquisa, iremos fazer o seguinte:
        (1) Criamos uma lista para armazenar os estados, para isso iremos pegar o nosso banco de dados e fazer uma listagem pegando
        somente os dados únicos 
            > list(df['state'].unique())
        (2) Criaremos então um list box, com o streamlit, para que possamos selecionar o estado a ser utilizado como referência na 
        pesquisa.
            > state = st.selectbox('Qual estado?', estados) 
                OBS: para fazer um menu na lateral colocamos st.sidebar....
                        st.sidebar.selectbox('Qual estado?', estados)

        

'''
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual estado?', estados)  

'''
    A partir então da criação da opção de seleção de estado, agora iremos criar uma nova caixa de opção para visualizar os dados 
    referentes a cada coluna. Para isso iremos fazer o seguinte: 
        (1) Iremos criar uma lista com os nomes de cada coluna
        (2) Da mesma forma que criamos a lista de estados, iremos criar uma listbox com os títulos das colunas:
            column = st.selectbox('Qual tipo de informação?', colunas)
'''
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)


'''
    A partir então da criação das opções de seleção de estado e coluna, iremos começar a parte da obtenção dos dados. Logo, uma vez que 
    selecionamos os dados da estado que queremos, iremos pegar a linha de informações referente ao estado escolhido
        
        df = df[df['state'] == state]

        > Explicando o código:
            Esse código está filtrando as linhas do DataFrame df que possuem um valor específico na coluna 'state'. O resultado é um novo
            DataFrame que contém apenas as linhas que satisfazem essa condição.

            Um DataFrame é uma estrutura de dados tabular bidimensional que pode ser pensada como uma planilha do Excel ou uma tabela de 
            banco de dados. Cada linha do DataFrame representa um registro (ou observação) e cada coluna representa uma variável. Por 
            exemplo, um DataFrame que contém informações sobre clientes de uma loja pode ter as seguintes colunas: nome, idade, sexo, 
            cidade, estado, compras_total.

            O código df[df['state'] == state] usa um operador de indexação para acessar apenas as linhas do DataFrame que atendem à 
            condição especificada. O operador de indexação [] é usado para selecionar um subconjunto de linhas ou colunas do DataFrame
            com base em uma condição. A condição aqui é que o valor da coluna 'state' seja igual ao valor de state.

            O resultado desse código é um novo DataFrame que contém apenas as linhas que atendem à condição especificada. Esse novo 
            DataFrame pode ser usado para análises e visualizações específicas ou para criar gráficos e tabelas que apresentam os 
            resultados de interesse.

 '''
df = df[df['state'] == state]

'''
    A partir da seleção feita acima, iremos abastecer o framework (plotly.express) que irá criar um grafico interativo (possibilitanto
    na web o acompanhmento com o mouse dos dados), onde iremos pegar do bando de dados (df) a data no eixo X e a coluna pre-selecionada 
    eixo Y 

    Por fim, o título do nosso gráfico será o nome da Coluna mais o estado (sendo contactenado da forma a seguir)
'''
fig = px.line(df, x="date", y=column, title=column + ' - ' + state)

# Criando um desing para o gráfico onde mudamos o nome dos exios e determinamos um tamanho para o título
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})



'''
    Para visualizarmos dentro do nosso código o gráfico podemos usar o seguinte comando:
        > fig.show()
'''

'''
    Aqui iremos usar a criação de textos usando o seguinte código:
        > st.title('DADOS COVID - BRASIL')                  >> TÍTULO
        > st.write('Nessa aplicação...)                     >> TEXTO
        > st.caption('Os dados...)                          >> RODAPÉ
''' 
st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

'''
    A seguir iremos então gerar nosso gráfico dentro do steamlite, na qual iremos usar o seguinte código:
        > st.plotly_chart(fig, use_container_width=True)
            >> fig dentro dessa função traz o gráfico previamente criado acima

'''
st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')

"""
    Para sinalizar para o streamlite que utlizamos uma biblioteca, temos que criar um arquivo txt para fazer essa concatenação
            > requirements.txt 
                Dentro do arquivo vamos colocar o seguinte:
                    plotly==5.8.0
"""
