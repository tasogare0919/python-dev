import boto3

log_group = 'log_group'
log_stream = 'log_stream'

client = boto3.client('logs')
response = client.get_log_events(
    logGroupName=log_group,
    logStreamName=log_stream,
    limit=10
)

for i in range(0, len(response['events'])):
    print(response['events'][i]['message']) 