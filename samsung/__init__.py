from samsung.miner import Samsung

if __name__ == '__main__':
    texts1 = Samsung.read_file()
    texts2 = Samsung.extract_hangul(texts1)
    token1 = Samsung.change_token(texts2)
    texts3 = Samsung.process_noun(token1)
    texts4 = Samsung.process_stopword(texts3)
    Samsung.show_wordcloud(texts4)