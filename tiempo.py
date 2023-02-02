primer=input()
segundo=input()
tercero=input()
cuerto=input()
if primer>segundo and primer>tercero and primer>cuerto:
    horapico=str("primera")
elif segundo>tercero and segundo>cuerto:
    horapico=str("segundo")
elif tercero>cuerto:
    horapico=str("tercero")
else:
    horapico=str("cuerto")
print(horapico)
