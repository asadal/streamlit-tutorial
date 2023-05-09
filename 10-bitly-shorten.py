import bitlyshortener
import configparser
import streamlit as st

config = configparser.ConfigParser()
config.sections()
config.read('./your_apikey.ini')

access_tokens = [config['bitly']['access_token']]
shortener = bitlyshortener.Shortener(tokens=access_tokens)

if url := st.text_input('URL을 입력해 주세요'):
    shortend = shortener.shorten_urls([url])
    st.markdown(
        '''
    ### URL이 생성되었습니다:sparkles:

    **긴 주소**
    '''
    )
    st.code(f'{url}')
    st.markdown('**짧은 주소**')
    st.code(f'{shortend[0]}')