"""
    In order to make synopsises group accessible, each synopsis needs it's own public/private key
    Each venture and project also needs to have pub/priv keys

    Security overview:
        On startup, if no internal database public/private key is found, it will be created
        The database private key is used to access Synopsis user IDs
"""