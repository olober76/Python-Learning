import time

def eksProgram():
    for i in range(10000):
        print("loop ke : ", i)


mulai = time.time()
eksProgram()
berhenti = time.time()

print(f"\n eksekusi Python Memerlukan waktu : {berhenti - mulai}")