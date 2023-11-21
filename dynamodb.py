import boto3

print("SI")

#create funtion for table list
def list_table():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)
        
list_table()





