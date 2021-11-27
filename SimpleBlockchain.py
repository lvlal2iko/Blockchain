# Python Simple Blockchain Code
import hashlib

class Block:
    def __init__(self, previous_block_hash, transaction_info):

        self.previous_block_hash = previous_block_hash
        self.transaction_info = transaction_info

        self.block_data = "\n".join(transaction_info) + "\n" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

transaction1 = "John send 10 BTC to Aliz"
transaction2 = "Alex send 15 BTC to Molly"
transaction3 = "Molly send 5.25 BTC to Jimmy"
transaction4 = "Jimmy send 30 BTC to Molly"
transaction5 = "Bell send 12 BTC to Alex"
transaction6 = "Jimmy send 3.5 BTC to Molly"

init_block = Block("Initial_hash-SHA256", [transaction1, transaction2])
print(init_block.block_data)
print(init_block.block_hash +"\n")


second_block = Block(init_block.block_hash, [transaction3, transaction4])
print(second_block.block_data)
print(second_block.block_hash +"\n")


third_block = Block(second_block.block_hash, [transaction5, transaction6])
print(third_block.block_data)
print(third_block.block_hash +"\n")
