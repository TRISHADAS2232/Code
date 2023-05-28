
def TOWER(N, BEG, AUX, END):
    if N == 1:
        print(BEG+"->"+END)
        return
    TOWER(N-1, BEG, END, AUX)
    print(BEG+"->"+END)
    TOWER(N-1, AUX, BEG, END)


#print(TOWER(4, "A", "B", "C"))
print(TOWER(3, "B", "A", "C"))
