import boto3
# ugo know too much 2
# create a boto3 client to access lambda
client = boto3.client('lambda')

def get_lambda_functions_by_tags(tags):

# set variable to store a list of lambda functions
  lambda_list = []

# list all lambda functions
  functions = client.list_functions()

# add to lambda_list all functions that have ProvisionedConcurrencyConfig enabled
  for function in functions['Functions']:

# get the function's configuration
    config = client.get_function_configuration(FunctionName=function['FunctionName'])

    if 'ProvisionedConcurrencyConfig' in config:

# check if tags match
      tags_match = True
      for tag in tags:
        if tag not in config['Tags']:
          tags_match = False
          break

# add function to list
      if tags_match:
        lambda_list.append(config)

# return list of lambda functions
  return lambda_list


if __name__ == '__main__':

# create list of tag keys and values
  tags = [
      {
          'Key': 'env',
          'Value': 'production'
      },
      {
          'Key': 'service',
          'Value': 'video-processing'
      }
  ]

  lambda_list = get_lambda_functions_by_tags(tags)
  print(lambda_list)
