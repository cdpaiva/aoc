from dataclasses import dataclass
import sys


@dataclass
class Block:
    id: int
    space: int
    is_free: bool


def main(blocks):
    new_blocks = []
    for i, n in enumerate(blocks):
        if i % 2 == 0:
            new_blocks.append(Block(id=i // 2, space=n, is_free=False))
        else:
            new_blocks.append(Block(id=-1, space=n, is_free=True))

    checksum = 0

    right = len(new_blocks) - 1
    while right > 0:
        curr: Block = new_blocks[right]
        if curr.is_free:
            right -= 1
            continue
        for i in range(1, right):
            block = new_blocks[i]
            if not block.is_free or block.space < curr.space:
                continue
            if block.space == curr.space:
                # move file to that block
                block.id = curr.id
                block.is_free = False
                # erase the current block memory
                curr.id = -1
                curr.is_free = True
                break
            elif block.space > curr.space:
                # create a new block with the file
                new_blocks.insert(i, Block(id=curr.id, space=curr.space, is_free=False))
                # erase current block location
                curr.id = -1
                curr.is_free = True
                # decrease free memory
                block.space -= curr.space
                break
        right -= 1

    i = 0
    for nb in new_blocks:
        if nb.id != -1:
            for j in range(nb.space):
                checksum += nb.id * (i + j)
        i += nb.space

    return checksum


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        blocks = [int(n) for n in list(f.read().rstrip())]

    print(main(blocks))
