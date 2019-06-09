from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

class Samsung:
    def __init__(self):
        pass

    @staticmethod
    def read_file():  # Text File 읽어오기
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = 'data/kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()
        print(texts[:100])
        print('--------------------')
        return texts

    @staticmethod
    def extract_hangul(texts):  # 한글만 추출
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        temp = tokenizer.sub('', temp)
        print(temp[:100])
        print('--------------------')
        return temp

    @staticmethod
    def change_token(texts):  # Token 변환
        tokens  = word_tokenize(texts)
        print(tokens[:30])
        print('--------------------')
        return tokens

    @staticmethod
    def process_noun(tokens):  # 명사 추출. 복합명사는 묶어서 Filtering 출력
        okt = Okt()
        noun_token = []
        for token in tokens:
            token_pos = okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos
                    if txt_tag[1] == 'Noun']
            if len("".join(temp)) > 1:
                noun_token.append("".join(temp))
        texts = " ".join(noun_token)
        print(texts[:100])
        print('--------------------')
        return texts

    @staticmethod
    def process_stopword(texts):
        with open('data/stopwords.txt', 'r', encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
        print(stopwords[:10])
        print('--------------------')
        # 필터링 텍스트를 살펴보기
        from nltk.tokenize import word_tokenize
        texts = word_tokenize(texts)
        print(texts[:8])
        print('--------------------')
        # Stopwords 를 활용하여 Token을 필터링
        texts = [text for text in texts
                 if text not in stopwords]
        # pandas 를 활용하여 상위빈도 객체를 출력한다
        import pandas as pd
        from nltk import FreqDist
        freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
        print(freqtxt[:25])
        print('--------------------')
        return texts

    @staticmethod
    def show_wordcloud(texts):
        wcloud = WordCloud('D2Coding.ttf',
                           relative_scaling=0.2,
                           background_color='white').generate(" ".join(texts))
        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()