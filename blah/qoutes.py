if __name__ == "__main__":
    qoutes = []
    with open('example.txt') as f:
        lines = f.readlines()
        for line in lines: 
            line = line.split("/;/")
            qoutes.append({"text":line[0], "author":line[1]})
    print(qoutes)
