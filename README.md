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


## State-Changing functions

### deposit

Deposit a token with its amount with an expected token address and amount. This is run by users.

| Key         | Type    | Description                             |
| ----------- | ------- | --------------------------------------- |
| token0      | address | Deposit token address                   |
| token1      | address | Expected token address                  |
| amount0     | uint256 | Deposit token amount                    |
| amount1_min | uint256 | Expected token amount for stop loss     |
| amount1_max | uint256 | Expected token amount for profit taking |

### cancel

Cancel order. This is run by users.

| Key        | Type    | Description          |
| ---------- | ------- | -------------------- |
| deposit_id | uint256 | Deposit Id to cancel |

### withdraw

Swap and send the token to the depositor. This is run by Compass-EVM only.

| Key                        | Type    | Description                                    |
| -------------------------- | ------- | ---------------------------------------------- |
| deposit_id                 | uint256 | Deposit Id to swap and send to the depositor   |
| profit_taking_or_stop_loss | bool    | True for profit taking and False for stop loss |

### multiple_withdraw

Swap and send multiple tokens to the depositor. This is run by Compass-EVM only.

| Key                        | Type      | Description                                             |
| -------------------------- | --------- | ------------------------------------------------------- |
| deposit_ids                | uint256[] | Deposit Ids array to swap and send to depositors        |
| profit_taking_or_stop_loss | bool[]    | Array of True for profit taking and False for stop loss |

### update_compass

Update Compass-EVM address.  This is run by Compass-EVM only.

| Key         | Type    | Description             |
| ----------- | ------- | ----------------------- |
| new_compass | address | New compass-evm address |

## Struct

### Deposit

| Key         | Type    | Description                                       |
| ----------- | ------- | ------------------------------------------------- |
| token0      | address | Token address to trade                            |
| token1      | address | Token address to receive                          |
| amount0     | uint256 | Token amount to trade                             |
| amount1_min | uint256 | Token amount to receive at least on stop-loss     |
| amount1_max | uint256 | Token amount to receive at least on profit taking |
| pool        | address | Dex(Uniswap V2) pool address                      |
| depositor   | address | Depositor address                                 |
