# TestMachineLearning1を関数化

from sklearn.metrics import accuracy_score

# アルゴリズムimport
from sklearn.svm       import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble  import RandomForestClassifier

import warnings
warnings.filterwarnings('ignore')


def load_input_data():
    # 学習データ（入力）
    # 3次元座標
    f = open('data/circle_data.csv', 'r')
    dataList = f.readlines()
    for data1 in dataList:
        data2 = []
        for num in range(3):
            data2.append(float(data1.rstrip('\n').split(',')[num]))
        input_data.append(data2)

    f.close()
    # print(input_data)


def load_output_data():
    # 学習データ（出力）
    # 3次元座標が半径1の球内であれば1（境界含む）、球外であれば2
    f = open('data/circle_answer.csv', 'r')
    dataList = f.readlines()
    for data1 in dataList:
        output_data.append(int(data1.rstrip('\n')))

    f.close()
    # print(output_data)


def load_test_data():
    f = open('data/circle_test.csv', 'r')
    dataList = f.readlines()
    for data1 in dataList:
        data2 = []
        for num in range(3):
            data2.append(float(data1.rstrip('\n').split(',')[num]))
        test_data.append(data2)

    f.close()
    # print(test_data)


input_data = []
load_input_data()

output_data = []
load_output_data()

# アルゴリズムの設定
algorithm_Li = LinearSVC()
algorithm_RF = RandomForestClassifier()
algorithm_KN = KNeighborsClassifier(n_neighbors=1)

# 学習
algorithm_Li.fit(input_data, output_data)
algorithm_RF.fit(input_data, output_data)
algorithm_KN.fit(input_data, output_data)

# テストデータ(予測したいデータ))
test_data = []
load_test_data()

# 予測結果
result1 = algorithm_Li.predict(test_data)
result2 = algorithm_RF.predict(test_data)
result3 = algorithm_KN.predict(test_data)
print("予測結果1:", result1)
print("予測結果2:", result2)
print("予測結果3:", result3)

# 正解：[2 1 2 2 1 2 1 2 2 2 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 1 1 2 2 1]
