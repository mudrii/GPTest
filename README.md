## Install python depandancyes

`
pip install openai gradio python-dotenv
`

## Export OpenAI API Key as Environment Variable
`
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
`
## Request Body Specification
The request body of ChaGPT API consists of the following parameters. Only the first two parameters are mandatory and the rest are for advanced usage.

* **model (string)** _[required]_: It denotes the ChatGPT model to be used. Usually, it will be gpt-3.5-turbo which always ensures you work with the stable version. However, you can give a specific version like gpt-3.5-turbo-0301 which is the current stable version that will be supported for the next few months until the next release of a new version. Future updates and releases of the model would be available on this OpenAI page.
* **messages (array)** _[required]_ : The input message prompt for generating ChatGPT completion in response. (Please see the next section for more details)
* **temperature (number)** : This is a value between 0 and 2 that controls the randomness of the response. A higher number will make the response quite random whereas a lower number makes the response deterministic. By default, the value is 1.
* **top_p (number)** : This is an alternative sampling method for the temperature discussed above. Here the model considers the output of the token with top_p probability mass. By default, the value is 1. (It is recommended to either use temperature or top_p instead of using both.)
* **n (integer)** : It denotes the number of chat response choices to be generated for each input prompt. By default is is 1.
* **stream (boolean)** : By default is is false but if set to true sents back generated chat completion data in a stream as they become available.
* **stop (string or array)** : It denotes up to four sequences where ChatGPT API will stop generating more tokens for completion. By default, it is null.
* **max_tokens (integer) **: It denotes the maximum allowed number of tokens in the response output.
* **presence_penalty (number)** : It is a value between  -2.0 and 2.0 that penalizes text depending on whether it has already appeared or not. A positive value can influence the model to talk about the new topic. By default, it is 0.
* **frequency_penalty (number)**: It is a value between  -2.0 and 2.0 that penalizes text depending on its frequency in the response so far. A positive value can influence the model to avoid repeating the same text. By default, it is 0.
* **logit_bias (map)**: It helps to change the likelihood of specified text’s presence in the output, By default it is null.
* **user (string)**: It is a unique identifier that denotes the end user and is helpful for tracking and monitoring abuse by OpenAI.


## What is Role in ChatGPT API ?
In ChatGPT API, each prompt object inside the message array has to be associated with one of the three roles – system, user, and assistant.

* _**System**_– Although it is not compulsory to pass a message with a system role, however, it is useful to set up the model behavior for conversation. In the above example, we told the model that it should act as our homework assistant.
* _**User**_ – The user role signifies that it is an input prompt from the end-user or it can also be a prompt triggered by an application.
* _**Assistant**_ – This role indicates that the message was a response by the assistant (model). This role is useful when you are required to save the prior conversation between the user and assistant in your application and again send it in a prompt request to maintain continuity. Alternatively, the assistant message can also be created manually by the developer to influence a desired behavior in the assistant’s subsequent responses.

## Note
### GPT-3.5
GPT-3.5 models can understand and generate natural language or code. Our most capable and cost effective model is gpt-3.5-turbo which is optimized for chat but works well for traditional completions tasks as well.

LATEST MODEL | DESCRIPTION | MAX REQUEST  | TRAINING DATA
------- | ------- | ------- | -------
gpt-3.5-turbo | Most capable GPT-3.5 model and optimized for chat at 1/10th the cost of text-davinci-003. Will be updated with our latest model iteration. | 4,096 tokens | Up to Sep 2021
g**pt-3.5-turbo-0301** | Snapshot of gpt-3.5-turbo from March 1st 2023. Unlike gpt-3.5-turbo, this model will not receive updates, and will only be supported for a three month period ending on June 1st 2023. | 4,096 tokens | Up to Sep 2021
text-davinci-003 | Can do any language task with better quality, longer output, and consistent instruction-following than the curie, babbage, or ada models. Also supports inserting completions within text. | 4,097 tokens | Up to Jun 2021
text-davinci-002 | Similar capabilities to text-davinci-003 but trained with supervised fine-tuning instead of reinforcement learning | 4,097 tokens | Up to Jun 2021
code-davinci-002 | Optimized for code-completion tasks | 8,001 tokens | Up to Jun 2021

### Codex
The Codex models are descendants of our GPT-3 models that can understand and generate code. Their training data contains both natural language and billions of lines of public code from GitHub. Learn more.

They’re most capable in _Python_ and proficient in over a dozen languages including _JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL,_ and even _Shell_.

Codex models:

LATEST MODEL | DESCRIPTION | MAX REQUEST | TRAINING DATA
------- | ------- | ------- | -------
code-davinci-002 | Most capable Codex model. Particularly good at translating natural language to code. In addition to completing code, also supports inserting completions within code. | 8,001 tokens | Up to Jun 2021
code-cushman-001 | Almost as capable as Davinci Codex, but slightly faster. This speed advantage may make it preferable for real-time applications. Up to | 2,048 tokens


### Run the chatbot code
`
python main.py
`


### Access Chat Boot in the browser
<http://127.0.0.1:7860>
