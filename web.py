from web3 import Web3

# Connect to the Ganache network using Web3
ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set the Ethereum address and private key of the admin
admin_address = '0xb8C078EDd829e1b58Ab4407b288e5850D596472d'  # Replace with the admin's address
admin_private_key = '0xa5ca62704ffcece00f7da010516863cc9c7fcc25a535184c3773e1c33e2ca5f7'  # Replace with the admin's private key

# Set the contract address and ABI
contract_address = '0xaAeacbAC129d512C8bd568788796cAe998175F6b'
contract_abi = '''[
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "adminAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "candidates",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "id",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "voteCount",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "candidatesCount",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "electionStarted",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "voters",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "string[]",
          "name": "_candidateNames",
          "type": "string[]"
        }
      ],
      "name": "startElection",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_candidateId",
          "type": "uint256"
        }
      ],
      "name": "vote",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getElectionStatus",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getElectionResults",
      "outputs": [
        {
          "internalType": "string[]",
          "name": "",
          "type": "string[]"
        },
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "endElection",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getCandidateIdsAndNames",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        },
        {
          "internalType": "string[]",
          "name": "",
          "type": "string[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "clearCandidates",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]'''
vadd = ["0x80426b9aA9c6424b940d37dCA8ECDCdE3246B071",
        "0xFc52ef06773270Ad9D5Be84D0b71F6513541aAB9",
        "0x74E00d9904D9BA81b0F3C4D3eE94C2eca78022D4",
        "0xb2d573db98D01cE9A29102De1fDC2A47ecD86eAb",
        "0xC01E00fba58820b6579f87E6275264D3BDC2DdD6",
        "0x83aa22B48C291f32435F9FBfAdebaB88737dD1B4",
        "0x8b4a3F2e4Cff4FB70AFd416bcAeD32Ff474a31F5",
        "0xbd5735F52B763a16533D9255c6fe053dB4c5AA3A",
        "0x7016DdBE337392811a07699719C91a1eA8Ef9eBf"
        ]

vpvt=["0xc490086324135cb8afb605feb026f9b1e8dd49714b177272651745a470b136fc",
      "0x7e59dde3971d7360ab5bf0d58e4bcadc4315685c885d3671d51155e3fa461aa8",
      "0x99d45803319ab8efb07cfb9d8a09cb3666720881310a0ef4e8b8ba3799c1d869",
      "0x662012f1ed29eb4799bf4c1e5f837e00f208131d08d75f224fc928dc75dea44c",
      "0xc2c729cc7f307b52aba3c8cf0dfc16a45c7f82be9d63071be1bb2419085c896f",
      "0x75378f1d9a9a8743d90217a2f77f12a50addb0ec59bb356b373f770e2d46ee78",
      "0x96d495149282f3376a9d9efb2792bb4465a7680b815fe75750dad816874be5ec",
      "0x3354f1bef9741bdcdfca232640285d499f18c8a45b4c9881d466295285bcef46",
      "0xa25c6183da0778b24e70268de617cfc56caa7e1922c7737465f8d530590f6255"]
# Create an instance of the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


def start_election(candidate_names):
    # Ensure that the provided candidate names list is not empty
    assert len(candidate_names) > 0, "Candidate names list cannot be empty"

    # Unlock the admin account
    web3.eth.defaultAccount = admin_address

    # Check if the election has already started
    election_started = contract.functions.getElectionStatus().call()
    if election_started:
        print("Election has already started. Please end the current election before starting a new one.")
        return

    # Start the election by calling the startElection function in the contract
    transaction = contract.functions.startElection(candidate_names).build_transaction({
        'from': admin_address,
        'nonce': web3.eth.get_transaction_count(admin_address),
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=admin_private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(transaction_hash)


def vote(candidate_id, vid):
    voter_private_key = vpvt[vid]
    # Ensure the candidate ID is valid
    candidates_count = contract.functions.candidatesCount().call()
    assert candidate_id > 0 and candidate_id <= candidates_count, "Invalid candidate ID"

    # Unlock the voter's account
    voter_address = web3.eth.account.from_key(voter_private_key).address

    # Check if the voter has already voted
    has_voted = contract.functions.voters(voter_address).call()
    if has_voted:
        print("Voter has already voted")
        return

    # Vote for the candidate by calling the vote function in the contract
    transaction = contract.functions.vote(candidate_id).build_transaction({
        'from': voter_address,
        'nonce': web3.eth.get_transaction_count(voter_address),
        'gas': 200000
    })
    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=voter_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)


def get_election_status():
    # Retrieve the current election status from the contract
    election_status = contract.functions.getElectionStatus().call()
    return election_status


def get_election_results():
    # Retrieve the election results from the contract
    candidate_names, vote_counts = contract.functions.getElectionResults().call()
    results = list(zip(candidate_names, vote_counts))
    return results


def end_election():
    # Unlock the admin account
    web3.eth.defaultAccount = admin_address

    # Check if the election has already ended
    election_ended = contract.functions.getElectionStatus().call()
    if not election_ended:
        print("Election has not started yet or has already ended.")
        return

    # End the election by calling the endElection function in the contract
    transaction = contract.functions.endElection().build_transaction({
        'from': admin_address,
        'nonce': web3.eth.get_transaction_count(admin_address),
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=admin_private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(transaction_hash)

def get_candidate_ids_and_names():
    # Retrieve the number of candidates from the contract
    candidates_count = contract.functions.candidatesCount().call()

    # Retrieve the candidate IDs and names from the contract
    candidate_ids = []
    candidate_names = []
    for i in range(1, candidates_count + 1):
        candidate = contract.functions.candidates(i).call()
        candidate_ids.append(candidate[0])
        candidate_names.append(candidate[1])

    # Combine the candidate IDs and names into a list of tuples
    candidates = list(zip(candidate_ids, candidate_names))

    return candidates

def clear_candidates():
    # Ensure that the election has not started
    election_started = contract.functions.getElectionStatus().call()
    if election_started:
        print("Cannot clear candidates while the election is ongoing.")
        return

    # Unlock the admin account
    web3.eth.defaultAccount = admin_address

    # Clear all candidate IDs and names by calling the clearCandidates function in the contract
    transaction = contract.functions.clearCandidates().build_transaction({
        'from': admin_address,
        'nonce': web3.eth.get_transaction_count(admin_address),
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=admin_private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(transaction_hash)

