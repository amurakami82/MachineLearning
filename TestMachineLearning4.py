# STLファイルを取り込み、メッシュをクラスタリング
# TestMachineLearning3.pyで使用したSTLの座標に、誤差程度の座標変化を付加

from sklearn.cluster import KMeans
import FIleImEx

# インプットデータ取得
importData = FIleImEx.import_file('data/many-plates_blur.stl')
vertexList = importData[0]  # メッシュ座標情報
facetList = importData[1]  # 法線情報

# メッシュ座標データと法線情報を結合した配列を作成
data = vertexList
for i in range(len(data)):
    data[i].extend(facetList[i])

clustering = KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300, tol=0.0001, verbose=0, random_state=None, copy_x=True)

# メッシュ座標情報+法線情報を使用
predictResult1 = clustering.fit_predict(data)
print(predictResult1)

# メッシュ座標情報のみを使用
predictResult2 = clustering.fit_predict(vertexList)
print(predictResult2)

# 法線情報のみを使用
predictResult3 = clustering.fit_predict(facetList)
print(predictResult3)

# 重心座標を使用
centerOfMassList = []
for i in range(len(vertexList)):
    centerOfMass = [(vertexList[i][0] + vertexList[i][3] + vertexList[i][6])/3,
                    (vertexList[i][1] + vertexList[i][4] + vertexList[i][7])/3,
                    (vertexList[i][2] + vertexList[i][5] + vertexList[i][8])/3]
    centerOfMassList.append(centerOfMass)
# print(centerOfMassList)
predictResult4 = clustering.fit_predict(centerOfMassList)
print(predictResult4)

# アウトプットデータ出力
vertexList_0 = []
vertexList_1 = []
facetList_0 = []
facetList_1 = []
for counter in range(len(predictResult4)):
    if predictResult4[counter] == 0:
        vertexList_0.append(vertexList[counter])
        facetList_0.append(facetList[counter])
    elif predictResult4[counter] == 1:
        vertexList_1.append(vertexList[counter])
        facetList_1.append(facetList[counter])

FIleImEx.export_file(vertexList_0, facetList_0, 'data/many-plates_blur_result_0.stl')
FIleImEx.export_file(vertexList_1, facetList_1, 'data/many-plates_blur_result_1.stl')
