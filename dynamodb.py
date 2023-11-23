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
#Crear funcion para insertar elemento en la tabla de dynamondb
def insert_item(nombre_tabla, id, nombre, apellido):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('nombre_tabla')
    table.put_item(
        Item={
            'id': '1',
            'name': 'Julieth',
            'age': '20'
        }
    )
    
#crear funcion para insertar elemento en la tabla de dynamondb
def insert_item(nombre_tabla, id, nombre, apellido):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    table.put_item(
        Item={
            'id': id,
            'name': nombre,
            'age': apellido
        }
    )
    print("Elemento insertado exitosamente")
    
#crear funcion para mostrar elementos de una tabla de dynamondb
def list_items(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    response = table.scan()
    items = response['Items']
    for item in items:
        print(item)
    print("Elementos mostrados exitosamente")
    

        

        
opcion=1
while opcion != 0:
    print("Ingrese la opción que desea")
    print("1. Listar tablas de dynamodb de la cuenta")
    print("2. Crear tabla de dynamodb")
    print("3. Insertar elemento en tabla de dynamodb")
    print("4. Mostrar elementos de una tabla de dynamodb") 
    print("0. Salir")
    opcion=int(input())
    if opcion == 1:
        list_table()
    elif opcion == 0:
        print("Saliendo...")
    if opcion == 2:
        nombre_tabla=input("Ingrese el nombre de la tabla a crear")
        create_table(nombre_tabla)
    if opcion == 3:
        nombre_tabla=input("Ingrese el nombre de la tabla a insertar")
        id=input("Ingrese el id del elemento a insertar")
        nombre=input("Ingrese el nombre del elemento a insertar")
        apellido=input("Ingrese el apellido del elemento a insertar")
        insert_item(nombre_tabla, id, nombre, apellido)
    if opcion == 4:
        nombre_tabla=input("Ingrese el nombre de la tabla a mostrar")
        list_items(nombre_tabla)
    else:
        print("Opcion no valida")
        
list_table()





