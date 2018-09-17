# love-lambda

Nothing can escape the system administrator's quest for total automation. Not even romance.

This lambda function pulls a daily quote about love down from the API at https://quotes.rest/qod and publishes it to an SNS. Subscribe your loved ones and show them you care.

## Configuration
Set up an SNS topic and subscribe your true love or loves. 

Create a lambda function with `love.py`. Define the environment variable `SNS_ARN` with the arn of your SNS. The lambda function needs permission to publish to the SNS, so give it the role `AWSLambdaSNSPublishPolicyExecutionRole`. 

Set up a CloudWatch event rule with the schedule `rate(1 day)`. If you do this through the Lambda console it should set up the permissions correctly for you.