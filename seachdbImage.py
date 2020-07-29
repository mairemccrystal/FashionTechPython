def test():
    newarray = []
    idthing = dbCollection.distinct("ID");

    #getNumResults = [x.strip() for x in str(idthing).split(',')]
    #numResults = (len(getNumResults))
   # print(numResults)

    for x in str(idthing).split(","):
        x = x.replace("'","")
        x = x.replace('[', "")
        x = x.replace(']', "")
        newarray.append(x)
