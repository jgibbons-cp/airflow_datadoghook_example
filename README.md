How to Configure Airflow for the Datadog Hook with Use Examples
--

Tested on Airflow 1.10.10 on Ubuntu 18.04.4 LTS on EC2

To instantiate an object the datadog_conn_id is required.  

 `def __init__(self, datadog_conn_id='datadog_default')`:

This is not a default connection in Airflow so it will throw an error saying the connection is undefined.

To configure 

1) go to the [connection UI](http://<airflow_host>:8080/admin/connection/).
2) Click create for a new connection
3) Then add the following:

[Airflow Connection UI](./connection.png)

From here you are ready to go.

Three very basic examples are in datadog_hook_example.py

Have fun!

