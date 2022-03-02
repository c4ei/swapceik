# sudo apt-get -y install python3-pip
# python3 -m pip install Web3
# wget https://unpkg.com/@uniswap/v2-core@1.0.0/build/Combined-Json.json
# python3 find_init_code_hash.py

import json
from web3 import Web3

f = open("/home/dev/www/uniswapV2/how_to_deploy/utils/Combined-Json.json", "r")
raw_data = f.read()
json_data = json.loads(raw_data)

string_hex = "0x" + json_data["contracts"]["contracts/UniswapV2Pair.sol:UniswapV2Pair"]["bytecode"]
temp_hex = Web3.keccak(hexstr=string_hex).hex()
print(temp_hex)

# The code below is what helped find the hash that is hard coded into Solidity because it was able to iterate through all of the JSON and hash automatically
# print(json_data);

# def iterate_multidimensional(my_dict):
#     for k,v in my_dict.items():
#         if(isinstance(v,dict)):
#             print("Key:" + k)
#             iterate_multidimensional(v)
#             continue
#         if "bytecode" in k:
#             if str(v).startswith("0x"):
#                 temp_hex = Web3.keccak(hexstr=str(v)).hex()
#                 if "9fc9c0c84af34af8c99dc393ed90a79572d208981d33d247a9c73617dbe9f3cf" in temp_hex:
#                     print("Key: " + k)
#                     print("Success ... 42ffe6804795e727b4765646b01aaf2dc7e13e6a002788bab6eb66e253472d5b")
#             else:
#                 temp_hex = Web3.keccak(hexstr="0x" + str(v)).hex()
#                 if "9fc9c0c84af34af8c99dc393ed90a79572d208981d33d247a9c73617dbe9f3cf" in temp_hex:
#                     print("Key: " + k)
#                     print("Success ... 9fc9c0c84af34af8c99dc393ed90a79572d208981d33d247a9c73617dbe9f3cf")

# iterate_multidimensional(json_data)
