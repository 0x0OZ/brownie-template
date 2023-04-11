#!/usr/bin/env python
from brownie import accounts, config, Contract, network  # type: ignore
LOCAL_NETWORKS = ["development", 'ganache-local', 'private']


def get_account(n=0):
    if network.show_active() in LOCAL_NETWORKS:
        return accounts[n]
    else:
        return accounts.add(config['wallets']['from'])


def get_contract(contract, *args, account=get_account(), contract_address="", contract_name="Monate", _deploy=False, n=-1):
    if _deploy:
        return deploy(contract, account, *args)
    if contract_address and contract_address != ('0x' + '0'*40):
        abi = contract.abi
        return Contract.from_abi(contract_name, contract_address, abi)
    try:
        return contract[n]
    except:
        return deploy(contract, account, *args)
    #return deploy(contract, account, *args)


def deploy(contract, account, *args):
    if len(args) == 0:
        return contract.deploy({"from": account})
    return contract.deploy(*args, {"from": account})


def get_details(contract, args, account=get_account()):
    for attr in args:
        for function_name, args in attr.items():
            function = getattr(contract, function_name)
            result = function(*args, {"from": account})
            _args = [str(arg) for arg in args]
            print(
                f"function {function_name}({','.join(_args)}) returned {result}")
