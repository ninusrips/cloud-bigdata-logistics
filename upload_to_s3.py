import boto3
s3 = boto3.client('s3')
s3.upload_file("orders.csv", "Ninusri", "raw/orders.csv")
print("Upload complete")
