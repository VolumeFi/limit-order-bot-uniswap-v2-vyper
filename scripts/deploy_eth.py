from ape import accounts, project, networks


def main():
    acct = accounts.load("deployer_account")
    priority_fee = networks.active_provider.priority_fee
    max_base_fee = int(networks.active_provider.base_fee * 1.2) + priority_fee
    compass = "0x652Bf77d9F1BDA15B86894a185E8C22d9c722EB4"
    uniswap_v2_router = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    fee = 10000000000000000
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 0
    project.limit_order_uniswap_v2.deploy(
        compass, uniswap_v2_router, refund_wallet, fee, service_fee_collector,
        service_fee, max_fee=max_base_fee,
        max_priority_fee=priority_fee, sender=acct)

# 0x74c6d395428A5343b81A333A2ea93Dbf107663c6