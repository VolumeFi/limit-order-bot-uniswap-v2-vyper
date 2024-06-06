from ape import accounts, project, networks


def main():
    acct = accounts.load("deployer_account")
    priority_fee = networks.active_provider.priority_fee
    max_base_fee = int(networks.active_provider.base_fee * 1.2) + priority_fee
    compass = "0x10812c485BF5cE3c5296a9f603b53344a15cC0cD"
    uniswap_v2_router = "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff"  # Quickswap
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    fee = 0
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 0
    project.limit_order_uniswap_v2.deploy(
        compass, uniswap_v2_router, refund_wallet, fee, service_fee_collector,
        service_fee, max_fee=max_base_fee,
        max_priority_fee=priority_fee, sender=acct)

# 0x37D3F3B7a5F091aBF36459430Da9BB883A710E69