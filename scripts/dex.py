#!/usr/bin/env python
import time
from brownie import Dex, DexToken, SwappableToken  # type: ignore
from scripts.scripts import get_account, get_contract, get_details
from web3 import Web3 as web3


def prepare(contract, token1, token2, owner, account=get_account()):
    if contract.token1() != token1.address and contract.token2() != token2.address:
        contract.setTokens(token1.address, token2.address, {"from": owner})
    if int(token1.balanceOf(contract.address)) < 100:
        token1.transfer(contract.address, 100, {"from": owner})
    if int(token2.balanceOf(contract.address)) < 100:
        token2.transfer(contract.address, 100, {"from": owner})
    if int(token1.balanceOf(account.address)) != 10:
        token1.transfer(account.address, 10, {"from": owner})
    if int(token2.balanceOf(account.address)) != 10:
        token2.transfer(account.address, 10, {"from": owner})
    return


def main():
    account = get_account()
    owner = get_account(1)  # only in development returns accounts[1]
    dex = get_contract(Dex, account=owner)  # (contract,args)
    token1 = get_contract(
        SwappableToken, dex.address, "Monate", "MET", 1000, account=owner)  # (contract,args)
    token2 = get_contract(
        SwappableToken, dex.address, "Valdoz", "VOZ", 1000, account=owner)  # (contract,args)
    swap_amount = 10
    attrs = {
        "schema": {"function_name": ["arg1", "arg2"]},
        "dex": [
            {"balanceOf": [token1.address, account.address]},
            {"balanceOf": [token2.address, owner.address]},
            {"getSwapPrice": [token1.address, token2.address, swap_amount]}
        ]
    }
    # the implementation of this function is not part of the template
    prepare(dex, token1, token2, owner, account=account)

    get_details(dex, attrs['dex'], account=owner)
    print("dex: ", dex)
    print("met: ", token1)
    print("voz: ", token2)


if __name__ == "__main__":
    main()
