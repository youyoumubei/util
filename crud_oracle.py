import cx_Oracle
import multiprocessing

# 插入数据的方法
def insert_data(data, connection_string):
    # 连接Oracle数据库
    connection = cx_Oracle.connect(connection_string)

    # 创建一个cursor对象
    cursor = connection.cursor()

    # 执行插入操作
    insert_query = "INSERT INTO table_name (column1, column2, column3) VALUES (:1, :2, :3)"
    cursor.executemany(insert_query, data)

    # 提交事务
    connection.commit()

    # 关闭cursor和连接
    cursor.close()
    connection.close()

# 读取文件中的数据
with open('data.txt') as f:
    data = f.readlines()

# 将数据分成多个块
num_threads = 4
chunk_size = len(data) // num_threads
chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# 启动多个线程并插入数据
connection_string = "用户名/密码@主机名:端口号/服务名"
pool = multiprocessing.Pool(num_threads)
for chunk in chunks:
    pool.apply_async(insert_data, args=(chunk, connection_string))
pool.close()
pool.join()
