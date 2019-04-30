import tensorflow as tf
import numpy as np

workers = ['127.0.0.1:50001', '127.0.0.2:50002', '127.0.0.2:50003']
cluster_spec = tf.train.ClusterSpec({'workers': workers})
server = tf.train.Server(cluster_spec, job_name='workers', task_index=1)
server.join()


