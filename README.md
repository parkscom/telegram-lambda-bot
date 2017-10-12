# apex-telegram-lambda-bot
This project is telegram simple-bot with Apex and AWS Lambda and python.

## Getting Started

### Project description
- telegram bot : two example 'echo bot' and 'flickr interest photo bot'
- Language : Python 3.x (tesed on 3.6)
- Run on AWS Lambda and [Apex](http://apex.run)

### Example telegram bot
- echo bot : https://t.me/parkscom_lambda_echo_bot
- flickr bot : https://t.me/parkscom_lambda_flickr_bot

### Install
#### First, Make sure that [Apex](http://apex.run) is installed.
```
$ curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh
```

#### Second, Change your IAM role and telegram token.
- project.json : 'role' field
- functions/echo/main.py, functions/echo/main.py : 'TELEGRAM_TOKEN', 'FLICKR_API_KEY' field

#### Third, deploy and build [API Gateway](https://aws.amazon.com/ko/api-gateway/)
Deploy your api with Apex
```
$ apex deploy
```

After deploying, you can find "telegrambot_echo" and "telegrambot_flickr" on your AWS Lambda console. Then, add trigger to AWS API Gateway with public access.
Now, you can get api url on API Gateway console. (eg. https://sometoken.execute-api.us-east-1.amazonaws.com/prod/telegrambot_flickr)

#### Finally, connect telegram setWebhook
Add telegram bot with webhook method like 'https://api.telegram.org/bot{YOUR_TELEGRAM_BOT_TOKEN}/setWebhook?url={YOUR_API_GATEWAY_URL}'
```
$ curl -XPOST "https://api.telegram.org/bot12345:FAKEkeyyupcjzzuyaIOXI/setWebhook?url=https://sometoken.execute-api.us-east-1.amazonaws.com/prod/telegrambot_flickr" -v
```

### Addtional note for Python pip package on Lambda
I used pip packages on Lamba deploy. Please see 'function.json'. On 'apex deploy', it will invoke trigger 'pip3 install'. ('setup.cfg' file is need for pip3 command. If that file is not exist, pip3 occured error.)

```json
{
    "description": "sample for telegram echo bot",
    "hooks":{
      "build": "pip3 install -r requirements.txt -t modules",
      "clean" : "rm -rf modules"
    }
  }
```

## See also
- Inspired project : [Creating a server-less Telegram bot with AWS Lambda and AWS API Gateway](https://medium.com/zingle/creating-a-server-less-telegram-bot-with-aws-lambda-and-aws-api-gateway-36406471b2ca) - It used by node.js and flickr APIs. That document is explain 'how to setup for Lambda and telegram bot'
- [Telegram bot documents](https://core.telegram.org/bots/api)
- [Telegram python bot module](https://github.com/python-telegram-bot/python-telegram-bot)
