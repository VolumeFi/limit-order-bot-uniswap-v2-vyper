from ape import accounts, project, networks


def main():
    acct = accounts.load("deployer_account")
    priority_fee = networks.active_provider.priority_fee
    max_base_fee = int(networks.active_provider.base_fee * 1.2) + priority_fee
    compass = "0x56Bff1a8D2af62584D7Ebf123452b765392e20E3"
    uniswap_v2_router = "0x4A7b5Da61326A6379179b40d00F57E5bbDC962c2"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    fee = 0
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 0
    project.limit_order_uniswap_v2.deploy(
        compass, uniswap_v2_router, refund_wallet, fee, service_fee_collector,
        service_fee, max_fee=max_base_fee,
        max_priority_fee=priority_fee, sender=acct)

# 0xF6f6895CfF43172818c43310a3C22d43c453344a