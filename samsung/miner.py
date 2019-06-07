from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re

class Samsung:
    def __init__(self):
        pass

    @staticmethod
    # Text File 읽어오기
    def read_file():
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = 'data/kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()
        return texts

    @staticmethod
    # 한글만 추출
    def extract_hangul(texts):
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        temp = tokenizer.sub('', temp)
        return temp

    @staticmethod
    # Token 변환
    def change_token(texts):
        tokens  = word_tokenize(texts)
        print(tokens[:200])