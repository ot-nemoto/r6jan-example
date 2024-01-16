import json

import requests
import os
import logging
logger = logging.getLogger()
logger.setLevel("DEBUG")

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        res = requests.get(os.environ['INVOKEE_ENDPOINT_URL'])
        logger.debug(res.text)
    except requests.RequestException as e:
        logger.error(e)
        raise e

    return {
        "statusCode": 200,
        "body": res.text,
    }