import requests
import os
import json
from pathlib import Path
from requests import Response
from dotenv import load_dotenv

load_dotenv()

PINATA_BASE_URL = 'https://api.pinata.cloud/'
endpoint = 'pinning/pinFileToIPFS'
img_filepath = './img/sample.png'
#json_filepath = './metadata/goerli/sample.json'
json_filepath = './scripts/sample.json'
img_filename = img_filepath.split('/')[-1:][0]
json_filename = img_filepath.split('/')[2].strip(".png")
headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
           'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}


def pinata_upload(nft_name, nft_description,nft_attributes, img_path):
    with Path(img_path).open("rb") as fp:
        image_binary = fp.read()
        response_1:Response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (img_filename, image_binary)},
            headers=headers,
        )
        print(response_1.json())

    image_hash:str = response_1.json()['IpfsHash']
    

    nft_attributes = {}
    

    json_arq:dict = {
            "name": nft_name,
            "description": nft_description,
            "image": "ipfs://" + image_hash,
            "attributes": [nft_attributes]     
    }

    with Path(json_filepath).open('w') as fp:
        json.dump(json_arq, fp)
    

    with Path(json_filepath).open("rb") as fp:
        json_binary = fp.read()
        response_2:Response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (json_filename + ".json", json_binary)},
            headers=headers,
        )
        print("\nPinata-cloud response: ")
        print(response_2.json())

    return response_2.json()['IpfsHash']
