import boto3
s3 = boto3.client('s3')
s3.upload_file("orders.csv", "your-bucket-name", "raw/orders.csv")
print("Upload complete")