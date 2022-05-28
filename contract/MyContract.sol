// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract scholar is ERC1155 {


    constructor() ERC1155("ipfs://Qmdf97SNz87DQTwXXmWSiTZAp3voqfkxGzNzniDWiCRrYc") {
        _mint(msg.sender, 1, 10000, "");
    }

    function safeTransferFrom(
        address from,
        address to,
        uint256 id,
        uint256 amount,
        bytes memory data
    ) public virtual override {
        _safeTransferFrom(from, to, id, amount, data);
    }


}