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

| Key           | Type      | Description                                 |
| ------------- | --------- | ------------------------------------------- |
| path          | address[] | Initial token swap path via Uniswap V2      |
| amount0       | uint256   | Deposit token amount                        |
| min_amount1   | uint256   | Expected token amount from the initial swap |
| profit_taking | uint256   | Permille of profit_taking                   |
| stop_loss     | uint256   | Permille of stop_loss                       |

### cancel

Cancel order. This is run by users.

| Key         | Type    | Description                                           |
| ----------- | ------- | ----------------------------------------------------- |
| deposit_id  | uint256 | Deposit Id to cancel                                  |
| min_amount0 | uint256 | Mininum amount of original token to receive on cancel |

### withdraw

Swap and send the token to the depositor. This is run by Compass-EVM only.

| Key           | Type         | Description                                             |
| ------------- | ------------ | ------------------------------------------------------- |
| deposit_id    | uint256      | Deposit Id to swap and send to the depositor            |
| min_amount0   | uint256      | Mininum amount of original token to receive on withdraw |
| withdraw_type | WithdrawType | Withdraw type enum value                                |

### multiple_withdraw

Swap and send multiple tokens to the depositor. This is run by Compass-EVM only.

| Key            | Type           | Description                                                   |
| -------------- | -------------- | ------------------------------------------------------------- |
| deposit_ids    | uint256[]      | Deposit Id array to swap and send to the depositor            |
| min_amounts0   | uint256[]      | Mininum amount array of original token to receive on withdraw |
| withdraw_types | WithdrawType[] | Withdraw type enum value array                                |

### update_compass

Update Compass-EVM address.  This is run by Compass-EVM only.

| Key         | Type    | Description             |
| ----------- | ------- | ----------------------- |
| new_compass | address | New compass-evm address |

## Struct

### Deposit

| Key       | Type      | Description                            |
| --------- | --------- | -------------------------------------- |
| path      | address[] | Initial token swap path via Uniswap V2 |
| amount    | uint256   | Ordered token amount                   |
| depositor | address   | Depositor address                      |

## Enum

### WithdrawType

| Key           | Description   |
| ------------- | ------------- |
| CANCEL        | Cancel order  |
| PROFIT_TAKING | Profit taking |
| STOP_LOSS     | Stop loss     |