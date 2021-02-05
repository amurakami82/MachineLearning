def import_file(fileName):
    # f = open('data/cube-ascii.stl', 'r')
    f = open(fileName, 'r')

    lCount = 0
    vertexCount = 0
    dataList = f.readlines()
    line = []
    vertexList = []
    facetList = []
    for data in dataList:
        data2 = data.rstrip('\n').strip(' ').split()
        # print(data2)
        if data2[0] == 'vertex':
            # print('lCount:' + str(lCount))
            del data2[0]
            line = line + list(map(float, data2))
            # print(list(map(float, data2)))
            # print(line)
            lCount = (lCount + 1) % 3
            # print(str(lCount))
            vertexCount = (vertexCount + 1) % 9
            if lCount == 0:
                # print(line)
                vertexList.append(line)
                line = []
        elif data2[0] == 'facet':
            del data2[0]
            del data2[0]
            facetList.append(list(map(float, data2)))

    f.close()
    # print(vertexList)

    return vertexList,facetList


def export_file(vertexList, facetList, fileName):
    # g = open('data/cube-ascii_after.stl', 'w')
    g = open(fileName, 'w')
    g.write('solid ' + fileName + '\n')

    print('len(vertexList):'+str(len(vertexList)))
    for counter in range(len(vertexList)):
        # g.write(facetList[counter])
        g.write('  facet normal  ')
        for xyzCounter in range(3):
            g.write(str('{:.6e}'.format(facetList[counter][xyzCounter])) + '  ')
        g.write('\n')
        g.write('    outer loop\n')
        for vertexCounter in range(3):
            g.write('      vertex   ')
            for xyzCounter in range(3):
                g.write(str('{:.6e}'.format(vertexList[counter][vertexCounter*3+xyzCounter])) + '  ')
            g.write('\n')
        g.write('    endloop\n')
        g.write('  endfacet\n')
    g.write('endsolid\n')
    g.close()




