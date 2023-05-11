// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "./ArmazenamentoDados.sol";

contract ArmazenamentoDadosFactory {

    ArmazenamentoDados[] public  armazenamentoDadosArray;

    function createArmazenamentoDadosContract() public{
        ArmazenamentoDados  armazenamentoDados = new  ArmazenamentoDados();
        armazenamentoDadosArray.push(armazenamentoDados);
    }

    function sfStore(uint256 _armazenamentoDadosIndex, string memory _nomeMateria, uint256 _nota) public{
        //addres
        //abi(Application Binary Interface)
        ArmazenamentoDados(address(armazenamentoDadosArray[_armazenamentoDadosIndex])).ArmazenarDados(_nomeMateria, _nota);
        
    }

    function sfGetMateria(uint256 _armazenamentoDadosIndex) public view returns (string memory){
        return ArmazenamentoDados(address(armazenamentoDadosArray[_armazenamentoDadosIndex])).NomeMateria();
    }
    function sfGetNota(uint256 _armazenamentoDadosIndex) public view returns (uint256){
        return ArmazenamentoDados(address(armazenamentoDadosArray[_armazenamentoDadosIndex])).Nota();
    }
    function sfGetPassou(uint256 _armazenamentoDadosIndex) public view returns (bool){
        return ArmazenamentoDados(address(armazenamentoDadosArray[_armazenamentoDadosIndex])).Passou();
    }
}