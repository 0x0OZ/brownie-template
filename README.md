# brownie-template
simple functions help automate some of the work when working with Brownie, at least those are the function I had to rewrite every time I do CTFs or start new projects

`get_account(n)`:
- simple widely used function with its implementation 
 
`get_contract(contract, *args, account=get_account(), contract_address="", contract_name="Monate", _deploy=False)`:
- it returns a contract object
- the arguments are the contract to deploy or to get deployed address, args for contract constructor if present
- others args are optional to set if needed, note you don't need to set \_deploy=true if no deployed contract exists

`deploy(contract,account, *args)`:
- you won't  really need to use this function, it's made to be used via `get_contract()`

`get_details(contract, args, account=get_account())`:
- it prints the return values of calling a set of functions, functions names, and arguments can be arbitrary but must be set in the attrs object
- this function took me several hours to figure out, there is a schema for what type of args it takes
- the args schema: 
```python
 attrs = {
        "some_name": {
    "function_name": ["arg1"],
    "function2_name": ["arg1", "arg2"],
    "function3_name": ["arg1","arg2","arg3"],
    },
    }
```
no more functions, it's minimal.
if you want more functions you can suggest, build yourself.
if you found something wrong or stupid, or have a question you can raise an issue, and you can send PR.
