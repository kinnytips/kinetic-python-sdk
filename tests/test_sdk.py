from kinetic_sdk import KineticSdk
from kinetic_sdk.models.transaction_type import TransactionType

from kinetic_sdk_generated.model.balance_response import BalanceResponse
from kinetic_sdk_generated.model.commitment import Commitment

from kinetic_sdk.models.keypair import Keypair
from solana.publickey import PublicKey

import logging as log

sdk = KineticSdk.setup(
    endpoint='http://localhost:3000',
    environment='local',
    index=1
)

mint = sdk.config.get('mint')
account = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'
owner = Keypair.random()


def test_get_balance():
    """ Test getting balance of an account """
    balance = sdk.get_balance(PublicKey(account))
    print(balance)
    assert type(balance) == BalanceResponse


def test_get_config():
    """ Test getting config of an account """
    config = sdk.config
    print(config)


def test_get_explorer_url():
    """ Test getting explorer url """
    url = sdk.get_explorer_url('/address/' + account)
    print(url)


def test_get_history():
    """ Test getting history of an account """
    history = sdk.get_history(account)
    # print(history)


def test_get_token_accounts():
    """ Test getting token accounts of an account """
    token_accounts = sdk.get_token_accounts(account)
    print(token_accounts)


def test_request_airdrop():
    """ Test requesting airdrop for an account """
    airdrop = sdk.request_airdrop(account, "100")
    print(airdrop)


def test_create_account():
    """ Test creating an account """
    account = sdk.create_account(owner)
    print(account)


def test_make_transfer():
    """ Test making a transfer """
    alice = Keypair.from_byte_array(
        [205, 213, 7, 246, 167, 206, 37, 209, 161, 129, 168, 160, 90, 103, 198, 142, 83, 177, 214, 203, 80, 29, 71, 245,
         56, 152, 15, 8, 235, 174, 62, 79, 138, 198, 145, 111, 119, 33, 15, 237, 89, 201, 122, 89, 48, 221, 224, 71, 81,
         128, 45, 97, 191, 105, 37, 228, 243, 238, 130, 151, 53, 221, 172, 125])
    transfer = sdk.make_transfer(
        owner=alice,
        destination='BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y',
        amount=17,
    )
    print(transfer)


def test_make_transfer_batch():
    """ Test making a batch transfer """
    alice = Keypair.from_byte_array(
        [205, 213, 7, 246, 167, 206, 37, 209, 161, 129, 168, 160, 90, 103, 198, 142, 83, 177, 214, 203, 80, 29, 71, 245,
         56, 152, 15, 8, 235, 174, 62, 79, 138, 198, 145, 111, 119, 33, 15, 237, 89, 201, 122, 89, 48, 221, 224, 71, 81,
         128, 45, 97, 191, 105, 37, 228, 243, 238, 130, 151, 53, 221, 172, 125])
    transfer = sdk.make_transfer_batch(
        owner=alice,
        destinations=[
            { 'destination': 'BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y', 'amount': '12' },
            { 'destination': 'CharYfTvJSiH6LtDpkGUiVVZmeCn5Cenu2TzdJSbDJnG', 'amount': '15' }
        ]
    )
    print(transfer)


def test_get_transaction():
    """ Test getting transaction """
    # transaction = sdk.get_transaction('4xQNnPHFwHvGcZwvwmcwJfXdwn758i9bYvk7htieBkFPUYQnMTB2eexMFuk2JsdrUSxuxeDU7yBcuBXYsmFUkYRT')
    # print(transaction)


def test_keypair_from_mnemonic():
    """ Test recovering a Keypair from mnemonic """
    TEST_MNEMONIC_PUBLIC_KEY = "5ZWj7a1f8tWkjBESHKgrLmXshuXxqeY9SYcfbshpAqPG"
    TEST_MNEMONIC_12 = 'pill tomorrow foster begin walnut borrow virtual kick shift mutual shoe scatter'
    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_12)
    assert str(keypair.public_key) == TEST_MNEMONIC_PUBLIC_KEY

def test_keypair_generate_mnemonic():
    """ Test generating a mnemonic """
    mnemonic = Keypair.generate_mnemonic()
    print(mnemonic)

def test_get_keypair_mnemonic():
    """ Test generating a mnemonic """
    keypair = Keypair()
    print(keypair.mnemonic)


def test_keypair_creation():
    """ Test creating a Keypair """
    keypair = Keypair()
    mnemonic = Keypair.generate_mnemonic()
    print('mnemonic: ', mnemonic)

    keypair = Keypair.from_mnemonic(mnemonic)
    print('keypair: ', keypair)

    commitment = Commitment('Finalized')
    print('commitment: ', commitment)

    account = sdk.create_account(
        owner=keypair, commitment=commitment)
    print('account: ', account)

