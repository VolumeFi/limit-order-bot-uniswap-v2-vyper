from ape import accounts, project, networks


def main():
    acct = accounts.load("deployer_account")
    priority_fee = networks.active_provider.priority_fee
    max_base_fee = int(networks.active_provider.base_fee * 1.2) + priority_fee
    compass = "0x1876e5fA704039dfF7da0C66d516AFAcBe23c59B"
    uniswap_v2_router = "0x10ED43C718714eb63d5aA57B78B54704E256024E"  # Pancakeswap
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    fee = 1000000000000000
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 0
    project.limit_order_uniswap_v2.deploy(
        compass, uniswap_v2_router, refund_wallet, fee, service_fee_collector,
        service_fee, max_fee=max_base_fee,
        max_priority_fee=priority_fee, sender=acct)

# 0xD29E9963D7d5da46897700c8AD958d5B91494132