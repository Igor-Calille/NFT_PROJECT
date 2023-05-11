#!/usr/bin/python3
from brownie import SimpleCollectible, accounts, network, config
from scripts.helpful_scripts import OPENSEA_FORMAT
from scripts.helpful_scripts import get_publish_source



def deploy_and_create_contract(pinata_resposne, priv_key):
    
    deploy(priv_key)
    dev = accounts.add(priv_key)
    print(network.show_active())
    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]
    token_id = simple_collectible.tokenCounter()
    transaction = simple_collectible.createCollectible(pinata_resposne, {"from": dev})
    transaction.wait(1)

    print(simple_collectible.address)

    print(
        "Postagem realizada! Agora voce pode ver sua nft em {}".format(
            OPENSEA_FORMAT.format(simple_collectible.address, token_id)
        )
    )
    print('Porfavor, espere por ate 10 minutos para a postagem da nft e clique no botao de recarregar a pagina')

    return "Postagem realizada! Agora voce pode ver sua nft em {}".format(
            OPENSEA_FORMAT.format(simple_collectible.address, token_id)
        )

def deploy(priv_key):
    dev = accounts.add(priv_key)
    print(network.show_active())
    SimpleCollectible.deploy({"from": dev}, publish_source=get_publish_source())




