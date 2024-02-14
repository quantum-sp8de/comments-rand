# comments-rand

Choose random winner (comment author) from youtube video available comments based on **TRUE random from quantum-sp8de**

## Installation

* **User** role must be installed as per instructions for [quantum-sp8de installation](https://github.com/quantum-sp8de/quantra-installer?tab=readme-ov-file#installation)
* Use the following command to install **comments-rand**:
  
  `pip3 install git+https://github.com/quantum-sp8de/comments-rand.git`

## Usage
Use help to see required options and their descriptions. Additionally, you can use environment variables insted specifying required arguments with **Q_** naming prefix (for example, **Q_PRIVATE_KEY**)
```
comments-rand --help
usage: comments_rand [-h] [-c CONTRACT_ACCOUNT] [-p PRIVATE_KEY] [-t TOKENS_ACCOUNT] [-b CHAIN_URL] [-a USER_ACCOUNT] [-y API_KEY] url

Choose random winner from the comments to youtube video

positional arguments:
  url                   youtube url

optional arguments:
  -h, --help            show this help message and exit
  -c CONTRACT_ACCOUNT, --contract_account CONTRACT_ACCOUNT
                        quantum-sp8de smart contract account
  -p PRIVATE_KEY, --private_key PRIVATE_KEY
                        private key for the user in blockchain
  -t TOKENS_ACCOUNT, --tokens_account TOKENS_ACCOUNT
                        account of tokens in blockchain
  -b CHAIN_URL, --chain_url CHAIN_URL
                        blockchain url
  -a USER_ACCOUNT, --user_account USER_ACCOUNT
                        user account in blockchain
  -y API_KEY, --api_key API_KEY
```
