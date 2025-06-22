#pip install streamlit
#pip install yfinance
import streamlit as st
import yfinance as yf

#  do Streamlit é fundamental para configurar a aparência e o comportamento da sua aplicação web. Ela deve ser a primeira chamada do Streamlit no seu script e só pode ser chamada uma vez por página (no caso de aplicativos de várias páginas, você a chama no início de cada arquivo de página).

st.set_page_config(
    page_title="PAINEL DE AÇÕES B3",
    layout='wide',
    page_icon='random'
)

st.header('**PAINEL DE PREÇOS DE FECHAMENTO E DIVIDENDOS DE AÇÕES DA B3 E A THAI CAGA GROSSO**')

ticker = st.text_input('Digite o ticker da ação', 'PETR4')
empresa = yf.Ticker(f'{ticker}.SA')

tickerDF = empresa.history(period='1d',
                           start='2019-01-01',
                           end='2025-06-19')

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write(f'**Empresa**: {empresa.info['longName'] if 'longName' in empresa.info else "N/A"}')

with col2:
    st.write(f'**Mercado**: {empresa.info['market']}')

with col3:
    st.write(f'**Preço Atual**: {empresa.info['currentPrice']}')

st.line_chart(tickerDF.Close) 
st.bar_chart(tickerDF.Dividends)    