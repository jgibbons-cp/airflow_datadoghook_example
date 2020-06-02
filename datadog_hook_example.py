from airflow.contrib.hooks.datadog_hook import DatadogHook

hook = DatadogHook()

title="Test airflow event"
text="This is a test event from the airflow hook"
alert_type="error"
tags=["airflow_test"]

#test event to the org event stream
#hook.post_event(title, text, aggregation_key=None, alert_type=alert_type, date_happened=None, \
#                handle=None, priority=None, related_event_id=None, tags=tags, device_name=None)

metric_name="airflow_hook_test_metric"
datapoint=1
tags=["airflow_test"]
metric_type="count"

#send a metric from the hook
#hook.send_metric(metric_name, datapoint, tags=tags, type_=metric_type, interval=None)

query="avg:airflow_hook_test_metric{*}.as_count()"
from_seconds_ago=3600
to_seconds_ago=0
response={}

#query a metric sent via the airflow datadog hook
#response = hook.query_metric(query, from_seconds_ago, to_seconds_ago)
#print(response)
