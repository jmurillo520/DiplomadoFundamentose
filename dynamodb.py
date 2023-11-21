import boto3

print("SI")

#create funtion for table list
def list_table():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)
        
#Crear funcion para crear tabla de dynamondb con capacidad bajo demanda
def create_table(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=nombre_tabla,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH' #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    print("Tabla creada exitosamente")

        
opcion=1
while opcion != 0:
    print("Ingrese la opción que desea")
    print("1. Listar tablas de dynamodb de la cuenta")
    opcion=int(input())
    if opcion == 1:
        list_table()
    elif opcion == 0:
        print("Saliendo...")
    if opcion == 2:
        nombre_tabla=input("Ingrese el nombre de la tabla a crear")
        create_table(nombre_tabla)
    else:
        print("Opcion no valida")
        
list_table()





