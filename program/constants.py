from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

#!!!SELECT MODE !!!#
MODE = "DEVELOPMENT"

#Close all open positions and orders
ABORT_ALL_POSITIONS = False

#Find Cointegrated pairs
FIND_COINTEGRATED = False

#PLACE TRADES
MANAGE_EXITS = True

#Place trades
PLACE_TRADES = True

#Resolution
RESOLUTION = "1HOUR"

#Stats window
WINDOW = 19

#Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1
USD_PER_TRADE = 100
USD_MIN_COLLATERAL = 1000

#Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

#Ethereum Adress
ETHEREUM_ADDRESS = "0x84860Dc5343adA44b98881BF18c39Dd00D153d0b"

#KEYS - PRODUCTION
#Tienes que estar en Mainnet
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")


#KEYS - DEVELOPMENT
#Tienes que estar en TESTNET
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

#KEYS - EXPORT
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

#HOST - EXPORT

HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_GOERLI

#HTTP - PROVIDER

HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/fdJa6EF5sCjUt0N6TkTI8IypugqSplAe"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/Sp0d_9QZx8G89O0yC1Sj_U6IjRroB0NZ"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET
