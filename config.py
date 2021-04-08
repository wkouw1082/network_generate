# basic hyper parameters
epochs = 500
dropout = 0.5
word_drop_rate=0

"""
model_param = {'batch_size': 30, 
               'lr': 0.001, 
               'weight_decay': 0.005, 
               'clip_th': 0.040380857476336032, 
               'emb_size': 116, 
               'en_hidden_size': 160, 
               'de_hidden_size': 225, 
               'rep_size': 171}
"""
model_param={'batch_size': 69, 'lr': 0.0013549389234627585, 'weight_decay': 0.010660900921725731, 'clip_th': 0.014512071116018106, 'emb_size': 165, 'en_hidden_size': 203, 'de_hidden_size': 227, 'rep_size': 20}

classifier_epochs=200
classifier_param={'batch_size': 26, 'lr': 0.00640815633081063, 'emb_size': 43, 'hidden_size': 92}

# graph_paremeter
data_dim = 25 # トポロジーの頂点数
classifier_bias=100
encoder_bias=3
# key: generate_topo(BA, fixed_BA, ...), value: [num, dim, [param]]
train_generate_detail = {"BA": [500, data_dim, [None]],\
                         "NN": [500, data_dim, [0.6]]}
test_generate_detail = {"fixed_BA": [100, data_dim, [None]],\
                        "NN": [100, data_dim, [0.6]]}
"""
train_generate_detail = {"BA": [2000, data_dim, [None]]}
valid_generate_detail = {"BA": [200, data_dim, [None]]}

train_generate_detail = {"NN": [2000, data_dim, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]]}
valid_generate_detail = {"NN": [200, data_dim, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]]}
"""

train_generate_detail = {"twitter_train":[None,None,[None]]}
valid_generate_detail = {"twitter_valid":[None,None,[None]]}

# データ分析時のdetail
visualize_detail = {"NN": [100, 100, [0.1,0.5,0.9]],
                    "twitter": [None,None,[None]]}
# NNのparamのkeyがだぶるので名前だけ別で定義
visualize_types = {"NN_0.1":'./data/csv/NN_0.1.csv',"NN_0.5":'./data/csv/NN_0.5.csv',"NN_0.9":'./data/csv/NN_0.9.csv',"twitter":'./data/csv/twitter.csv'}

ignore_label=1000

opt_epoch=100

# コンディショナルで指定する値
power_degree_label = [1.2,0.8,0.3]
power_degree_dim = len(power_degree_label)
cluster_coefficient_label = [0.2,0.4,0.6]
cluster_coefficient_dim = len(cluster_coefficient_label)

# 評価を行うパラメータら
# 現状、"power_degree", "cluster_coefficient", "distance", "size"
eval_params = ["power_degree", "cluster_coefficient", "distance","average_degree","density","modularity","maximum_distance","degree_centrality","betweenness_centrality","closeness_centrality", "size"]
# 評価を行うパラメータの外れ値を除くために値の上限を設定 指定は値を[最小値,最大値]の形で、指定なしはNoneで
# 仕様変更がめんどくさいので別で定義　いつか誰か一つにして欲しい
eval_params_limit = {"power_degree":None,"cluster_coefficient":[0,0.5],"distance":[0,8],\
                    "average_degree":[0,10],"density":[0,0.1],"modularity":[0,1],"maximum_distance":None,\
                    "degree_centrality":None,"betweenness_centrality":None,"closeness_centrality":None, "size":None}
# 評価に用いるネットワークのサイズの閾値
size_th=0
# 評価に用いるネットワーク数
graph_num=300
# 生成する最大dfsコード長
generate_max_len=500

reddit_path = "./data/reddit_threads/reddit_edges.json"
twitter_path = "./data/Twitter/edgelists/renum*"

# 次数分布の冪指数を出すときに大多数のデータに引っ張られるせいで１次元プロットが正しい値から離れてしまうのでいくつかの値を除いて導出するための除く割合
power_degree_split_raito = {"NN":0.04,"twitter":10}