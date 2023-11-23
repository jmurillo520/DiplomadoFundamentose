#read csv
import csv
import json

def read_csv(path):
    with open('usuarios.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            
def  lambda_handler(event, context):
    read_csv('usuarios.csv')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }