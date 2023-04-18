from brownie import limit_order_uniswap_v2, accounts


def main():
    acct = accounts.load("deployer_account")
    limit_order_uniswap_v2.deploy(
        "0x370A1a665328170eFA6a0bb51f948108C23528BA",
        "0x10ED43C718714eb63d5aA57B78B54704E256024E",
        {"from": acct}
    )
