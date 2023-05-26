from brownie import limit_order_uniswap_v2, accounts


def main():
    acct = accounts.load("deployer_account")
    limit_order_uniswap_v2.deploy(
        "0xBE3AeB2953B6757AA7Eaf4c69a66D6316c98363e",
        "0x10ED43C718714eb63d5aA57B78B54704E256024E",
        {"from": acct}
    )
