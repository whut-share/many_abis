from .. import W_ERC20_ABI


SUPPORT_DEX = ['mdex_heco']

WETH = {
    'name': 'Wrapped HT',
    'symbol': 'WHT',
    'address': '0x5545153CCFcA01fbd7Dd11C0b23ba694D9509A6F',
    'abi': W_ERC20_ABI,
}

COINS = {
    'USDT HECO': '0xa71edc38d189767582c38a3145b5873052c3e47a',
    'USDC HECO': '0x9362bbef4b8313a8aa9f0c9808b80577aa26b73b',
    'DAI HECO': '0x3d760a45d0887dfd89a2f5385a236b29cb46ed2a'

}

BASIC = {
    'chain': 'Huobi Eco Chain',
    'explorer': 'https://hecoinfo.com/',
    'weth' : WETH,
    'coins': COINS
}
