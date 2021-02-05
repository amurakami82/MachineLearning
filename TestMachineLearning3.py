# STLファイルを取り込み、メッシュをクラスタリング
# メッシュの法線は2種類のみのため、法線でクラスタリングすることを想定

from sklearn.cluster import KMeans
import FIleImEx

# インプットデータ取得
importData = FIleImEx.import_file('data/two-plates.stl')
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

# アウトプットデータ出力
FIleImEx.export_file(vertexList, facetList, 'data/two-plates_result.stl')

