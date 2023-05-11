// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract ArmazenamentoDados{
    
    // this will get initialized to 0!

    string nomeMateria;
    uint256 nota;
    bool passou;
    

    function NomeMateria() public view returns(string memory) {
        return nomeMateria;
    }

    function Nota() public view returns(uint256) {
        return nota;
    }

    function Passou() public view returns(bool){
        bool test;
        if (nota >= 5) test = true;
        else test = false;

        return test; 
    }
    
    function ArmazenarDados(string memory _nomeMateria, uint256 _nota) public{
        nomeMateria = _nomeMateria;
        nota = _nota;
    }    
    
}