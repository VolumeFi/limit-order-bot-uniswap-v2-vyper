# Limit Order Bot Vyper for Uniswap V2

## Dependencies

[Brownie](https://github.com/eth-brownie/brownie)

[Ganache](https://github.com/trufflesuite/ganache)

## Add account

```sh
brownie accounts new deployer_account
```

## Deploy on mainnet
Create `scripts/deploy_*.py` and Compass-EVM contract address.
### - Pancakeswap V2
```sh
brownie run scripts/deploy_pancakeswap.py --network bsc-main
```

## Read-Only functions

### compass

| Key        | Type    | Description                                |
| ---------- | ------- | ------------------------------------------ |
| **Return** | address | Returns compass-evm smart contract address |

### admin

| Key        | Type    | Description              |
| ---------- | ------- | ------------------------ |
| **Return** | address | Returns an admin address |

### deposit_size

| Key        | Type    | Description                       |
| ---------- | ------- | --------------------------------- |
| **Return** | uint256 | Returns deposit list current size |

### deposits

| Key        | Type    | Description                           |
| ---------- | ------- | ------------------------------------- |
| *arg0*     | uint256 | Deposit Id to get Deposit information |
| **Return** | Deposit | Deposit information                   |

### ignores

| Key        | Type    | Description                                     |
| ---------- | ------- | ----------------------------------------------- |
| *arg0*     | uint256 | Deposit Id to check if it is in the ignore list |
| **Return** | bool    | True if it is in the ignore list                |

## State-Changing functions

### deposit

Deposit a token with its amount with an expected token address and amount. This is run by users.

| Key     | Type    | Description            |
| ------- | ------- | ---------------------- |
| token0  | address | Deposit token address  |
| token1  | address | Expected token address |
| amount0 | uint256 | Deposit token amount   |
| amount1 | uint256 | Expected token amount  |

### cancel

Cancel order.

| Key        | Type    | Description          |
| ---------- | ------- | -------------------- |
| deposit_id | uint256 | Deposit Id to cancel |

### withdraw

Swap and send the token to the depositor.

| Key        | Type    | Description                                  |
| ---------- | ------- | -------------------------------------------- |
| deposit_id | uint256 | Deposit Id to swap and send to the depositor |

### multiple_withdraw

Swap and send multiple tokens to the depositor.

| Key         | Type      | Description                                      |
| ----------- | --------- | ------------------------------------------------ |
| deposit_ids | uint256[] | Deposit Ids array to swap and send to depositors |

### ignore_deposit

Ignore a deposit id from withdraw list in case the expected token is a fee charged token. It will revert withdraw transaction so it can be canceled only after ignored.

| Key        | Type    | Description                             |
| ---------- | ------- | --------------------------------------- |
| deposit_id | uint256 | Deposit Id to ignore from withdraw list |

### update_admin

Update admin address.

| Key       | Type    | Description       |
| --------- | ------- | ----------------- |
| new_admin | address | New admin address |

### update_compass

Update Compass-EVM address.

| Key         | Type    | Description             |
| ----------- | ------- | ----------------------- |
| new_compass | address | New compass-evm address |

## Struct

### Deposit

| Key       | Type    | Description                      |
| --------- | ------- | -------------------------------- |
| token0    | address | Token address to trade           |
| token1    | address | Token address to receive         |
| amount0   | address | Token amount to trade            |
| amount1   | address | Token amount to receive at least |
| pool      | address | Dex(Uniswap V2) pool address     |
| depositor | address | Depositor address                |
