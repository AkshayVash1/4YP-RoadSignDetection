import os

dir_path = r"C:\Users\Akshay\.vscode\4YP-RoadSignDetection\4YP-RoadSignDetection\yield-sign\valid\labels"
save_path = r"C:\Users\Akshay\.vscode\4YP-RoadSignDetection\4YP-RoadSignDetection\saves"

res = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

for file in res:
    with open(dir_path + "\\" + file, 'r') as rf:
            lines = rf.readlines()
            rf.close()
            if not lines:
                print("FILE IS EMPTY\n")
                print("Filename: " + file + "\n")
            else:
                os.chdir(save_path)
                with open(file, "w") as wf:
                    for line in lines:
                        if line[0] == "0":
                            newline = line.replace("0", "4", 1) 
                            wf.write(newline)
                        else: 
                            wf.write(line)
                    wf.close()
                            
                    
