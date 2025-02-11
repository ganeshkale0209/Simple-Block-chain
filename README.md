# Simple-Block-chain
This project is a simple blockchain simulation written in Python. It demonstrates the core features of a blockchain, including block creation, hashing, proof-of-work, and tamper detection. The simulation also supports real-time transaction processing

Features
Block Structure:
Index
Timestamp
List of transactions
Previous block hash
Current block hash
Nonce (for proof-of-work)

Hashing:
SHA-256 is used to generate block hashes.

Proof-of-Work:
Blocks are mined to meet a difficulty criterion (e.g., hash starting with a certain number of zeros).

Real-Time Transactions:
Transactions are added dynamically and grouped into blocks.

Tamper Detection:
The blockchain validates its integrity and detects tampering.

Prerequisites
Python 3.x
hashlib (included in Python standard library)
datetime (included in Python standard library)
json (included in Python standard library)

Setup and Execution
1. Run the Simulation
python app.py

Code Structure
Block: Represents a single block in the blockchain.
compute_hash(): Computes the SHA-256 hash of the block.
mine_block(difficulty): Mines the block using proof-of-work.
Blockchain: Manages the chain of blocks.
create_genesis_block(): Initializes the blockchain with a genesis block.
add_transaction(transaction): Adds a transaction to the pending list.
_add_block(): Mines a new block with pending transactions.
is_valid(): Validates the integrity of the blockchain.
print_chain(): Prints all blocks in the blockchain.

Sample Input
Transactions are added dynamically in the main function:
transactions = [
    "Alice sent 1 BTC to Bob",
    "Bob sent 2 BTC to Charlie",
    "Charlie sent 0.5 BTC to Alice",
    "Dave sent 3 BTC to Eve"
]

Sample Output
Adding transactions in real-time...
Added transaction: Alice sent 1 BTC to Bob
Added transaction: Bob sent 2 BTC to Charlie
Added transaction: Charlie sent 0.5 BTC to Alice
Added transaction: Dave sent 3 BTC to Eve

Final Blockchain:
Block #0
Timestamp: 2025-02-10T12:34:56.789000
Transactions: ['Genesis Transaction']
Previous Hash: 0
Hash: 0000a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6

Block #1
Timestamp: 2025-02-10T12:35:01.123000
Transactions: ['Alice sent 1 BTC to Bob', 'Bob sent 2 BTC to Charlie']
Previous Hash: 0000a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
Hash: 0000b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a1

Block #2
Timestamp: 2025-02-10T12:35:05.456000
Transactions: ['Charlie sent 0.5 BTC to Alice', 'Dave sent 3 BTC to Eve']
Previous Hash: 0000b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a1
Hash: 0000c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a1b2

Is blockchain valid? True
Is blockchain valid after tampering? False

Contact
For questions or feedback, feel free to reach out:
Your Name : Ganesh kale
Email: ganeshkale0209@ggmail.com
GitHub: ganeshkale0209

