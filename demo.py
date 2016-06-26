from api.ai import Agent
import json


##
agent = Agent(
     '<subscription-key>',
     '9c4ddb316ec54081adee6273b7a768e5',
     '5b9406958d62462f8bb72dd3e63a9a57',
)

def saveType(flowerType):
	print 'do something here'

def saveColor(color):
	print 'do something here'

def createOrder(address):
	print 'do something here'

def main():
	user_input = ''

	while user_input != 'exit':

		user_input  = raw_input("me: ")
		response = agent.query(user_input)
		result = response['result']
		fulfillment = result['fulfillment']

		print 'bot: ' + fulfillment['speech']

		if result['action'] == 'saveFlowerType':
			saveType(user_input)
		if result['action'] == 'saveColor':
			saveColor(user_input)
		if result['action'] == 'createOrder':
			createOrder(user_input)


if __name__ == "__main__":
    main()