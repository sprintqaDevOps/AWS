import json, boto3

ses = boto3.client('ses')

FROM_EMAIL_ADDRESS = ''

#customerEmail=''

def lambda_handler(event, context):
	#Step 1: Parse given query string parameters
	purchaseId = event['queryStringParameters']['purchaseId']
	purchaseItem = event['queryStringParameters']['item']
	purchaseAmount = event['queryStringParameters']['amount']
	customerEmail = event['queryStringParameters']['email']

	print('purchaseId=' + purchaseId)
	print('purchaseItem=' + purchaseItem)
	print('purchaseAmount=' + purchaseAmount)
	print('customerEmail='+customerEmail)

	#Step2: Create body of the response object
	purchaseResponse = {}
	purchaseResponse['orderNumber'] = purchaseId
	purchaseResponse['item'] = purchaseItem
	purchaseResponse['amount'] = purchaseAmount
	purchaseResponse['email'] = customerEmail
	purchaseResponse['message'] = 'We have received your order, thank you.'

	#Step 3: Create http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(purchaseResponse)
	
	#Step 4: Send email confirmation with SES
	orderPlacementText='Hello, your order is placed successfully. We will ship your item as soon as possible, thank you for your business.'
	ses.send_email( Source=FROM_EMAIL_ADDRESS,
		Destination={ 'ToAddresses': [customerEmail] }, 
		Message={ 'Subject': {'Data': 'Your order is placed.'},
		    'Body': {'Text': {'Data': orderPlacementText}}
		}
	    )
	
	#Step 5: Return the response object
	return responseObject
