// SPDX-License-Identifier: MIT
pragma solidity 0.6.6; //Não se preocupe caso aponte um erro

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    //Declaração de variáveis
    uint256 public tokenCounter;

    //Construtor do contrato que utiliza as especificações dos contratos formulados em ERC-721
    //Especificaçoes do ERC-721 <-- https://eips.ethereum.org/EIPS/eip-721
    constructor () public ERC721 ("NFT_Tmaker","NTM"){//Nome e símbolo da coleção de NFT's
        tokenCounter = 0;
    }


    function createCollectible(string memory tokenURI) public returns (uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newItemId;
    }


    

}
