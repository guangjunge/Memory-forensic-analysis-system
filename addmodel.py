from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)




# 定义特征数据预处理函数
def preprocess_features(features):
    # 在这里可以对特征数据进行必要的预处理，如归一化、reshape等操作
    preprocessed_features = features
    return preprocessed_features

# 加载训练好的TensorFlow模型
model = tf.keras.models.load_model('/mdel/trained/SAAE_stacking.h5')
# 定义路由，接收POST请求
@app.route('/classify', methods=['POST'])
def classify():
    # 从请求中获取特征数据
    feature_data = request.json['features']

    # 对特征数据进行预处理
    preprocessed_data = preprocess_features(feature_data)

    # 使用加载的模型进行分类预测
    predictions = model.predict(np.array([preprocessed_data]))

    # 返回预测结果
    result = {'class': int(np.argmax(predictions[0]))}  # 假设预测结果是类别的索引
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)








import subprocess

def create_memory_dump_win(dumpit_path, output_file ):
    #dumpit_path为dumpit.exe的实际路径
    #output_file为生成的内存转储文件名

    # 使用Popen函数执行dumpit.exe命令
    process = subprocess.Popen([dumpit_path, "/accepteula", "/output", output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # 与子进程交互，获取输出和错误
    output, error = process.communicate()
    if process.returncode == 0:
        # 打印命令输出
        print("dumpit.exe command output:")
        print(output.decode('utf-8'))
    else:
        # 打印错误信息
        print("Error executing dumpit.exe command:")
        print(error.decode('utf-8'))

# 调用函数生成内存转储
create_memory_dump()




import subprocess
import platform

def create_memory_dump_Linux(lime_path, output_file):
    kernel_version = platform.uname().release
    if int(kernel_version.split('.')[0]) < 2 or (int(kernel_version.split('.')[0]) == 2 and int(kernel_version.split('.')[1]) < 6):
        # Linux内核版本早于2.6，使用dd命令拷贝/dev/mem获取内存镜像
        dd_command = f"dd if=/dev/mem of{output_file}"
        process = subprocess.Popen(dd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        # Linux内核版本为2.6及以后，使用lime工具获取内存
        lime_command = f"{lime_path} -o {output_file}"  # 构建lime命令
        process = subprocess.Popen(lime_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    output, error = process.communicate()

    if process.returncode == 0:
        # 打印命令输出
        print("Command output:")
        print(output.decode('utf-8'))
    else:
        # 打印错误信息
        print("Error executing command:")
        print(error.decode('utf-8'))

# 调用函数获取内存镜像
get_memory_dump()



lime_path = "/path/to/lime"  # lime工具的实际路径
    lime_command = f"{lime_path} -o {output_file}"  # 构建lime命令

    process = subprocess.Popen(lime_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, error = process.communicate()















