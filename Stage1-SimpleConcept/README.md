The simple ideas of distributed Tensorflow
===

The simple ideas of distrubtued Tensorflow is to build several servers. The users just need to manipulate the service via tf.Session().

# The processes 
1. Executing the scripts of TF-distribute-server*.py. These scripts will create local services of tensorflow using the ports of 50001, 50002, 50003.

2. Executing the computing script "TF-HQ.py". This script use the TF-distribute-server1.py (which bind to the 50001 port) as main server to triger other services on other servers.


