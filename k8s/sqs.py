import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.sa-east-1.amazonaws.com/226232566259/credit-consult-proposal-credit_dlq'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=4,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
message1 = response['Messages'][1]
message2 = response['Messages'][2]
message3 = response['Messages'][3]

receipt_handle = message['ReceiptHandle']

print('Received message: %s' % message )
print('Received message: %s' % message1 )
print('Received message: %s' % message2 )
print('Received message: %s' % message3 )