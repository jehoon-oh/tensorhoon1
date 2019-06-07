from samsung.miner import Samsung

if __name__ == '__main__':
    t = Samsung.read_file()
    t_hangul = Samsung.extract_hangul(t)
    Samsung.change_token(t_hangul)