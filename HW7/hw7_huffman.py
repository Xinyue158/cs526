#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
import json
import heapq
from dataclasses import dataclass
from collections import Counter
from typing import Dict, Optional, Tuple


@dataclass
class Node:
    freq: int
    char: Optional[str] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text_file(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def build_frequency_map(text: str) -> Dict[str, int]:
    return dict(Counter(text))


def build_huffman_tree(freq_map: Dict[str, int]) -> Node:
    """
    Build Huffman tree using a heap of tuples (freq, tie_id, node)
    to avoid comparing Node objects directly (prevents None vs str errors).
    """
    heap = []
    tie = 0

    for ch, freq in freq_map.items():
        heapq.heappush(heap, (freq, tie, Node(freq=freq, char=ch)))
        tie += 1


    if not heap:
        return Node(freq=0, char=None)


    if len(heap) == 1:
        _, _, only = heapq.heappop(heap)
        return Node(freq=only.freq, char=None, left=only, right=None)


    while len(heap) > 1:
        f1, _, a = heapq.heappop(heap)
        f2, _, b = heapq.heappop(heap)
        parent = Node(freq=f1 + f2, char=None, left=a, right=b)
        heapq.heappush(heap, (parent.freq, tie, parent))
        tie += 1

    return heap[0][2]


def build_code_map(root: Node) -> Dict[str, str]:
    codes: Dict[str, str] = {}

    def dfs(node: Optional[Node], path: str) -> None:
        if node is None:
            return


        if node.char is not None:
            codes[node.char] = path if path != "" else "0"
            return

        dfs(node.left, path + "0")
        dfs(node.right, path + "1")

    dfs(root, "")
    return codes


def encode_text(text: str, codes: Dict[str, str]) -> str:
    return "".join(codes[ch] for ch in text)


def decode_bits(bits: str, root: Node) -> str:
    if not bits:
        return ""


    if root.char is None and root.left is not None and root.right is None and root.left.char is not None:
        return root.left.char * len(bits)

    out_chars = []
    node = root
    for b in bits:
        node = node.left if b == "0" else node.right

        if node is None:
            raise ValueError("Decoding error: reached a null node. Compressed data may be corrupted.")

        if node.char is not None:
            out_chars.append(node.char)
            node = root

    return "".join(out_chars)


def print_input_set(text: str) -> None:
    print("===== INPUT SET =====")
    print("Total characters:", len(text))
    print("Unique characters:", len(set(text)))
    preview = text[:400].replace("\n", "\\n")
    print("Preview (first 400 chars):")
    print(preview)
    print()


def print_frequency_map(freq_map: Dict[str, int], top_k: int = 20) -> None:
    print("===== FREQUENCY MAP =====")
    print("Total unique chars:", len(freq_map))
    items = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))
    print(f"Top {min(top_k, len(items))} characters by frequency:")
    for ch, f in items[:top_k]:
        show = ch
        if ch == "\n":
            show = "\\n"
        elif ch == "\t":
            show = "\\t"
        elif ch == " ":
            show = "(space)"
        print(f"  {show!r}: {f}")
    print()


def print_tree_codes(codes: Dict[str, str]) -> None:
    """
    For homework printing: show the Huffman "tree" as codes (char -> bitstring).
    This is the clearest readable representation for terminal screenshots.
    """
    print("===== HUFFMAN TREE (CODES VIEW) =====")
    items = sorted(codes.items(), key=lambda x: (len(x[1]), x[0]))
    for ch, code in items:
        show = ch
        if ch == "\n":
            show = "\\n"
        elif ch == "\t":
            show = "\\t"
        elif ch == " ":
            show = "(space)"
        print(f"  {show!r}: {code} (len={len(code)})")
    print()


def write_compressed_file(path: str, freq_map: Dict[str, int], bitstring: str) -> None:
    header = json.dumps(freq_map, ensure_ascii=False)
    with open(path, "w", encoding="utf-8") as f:
        f.write("===FREQ_MAP_JSON===\n")
        f.write(header + "\n")
        f.write("===DATA_BITS===\n")
        f.write(bitstring + "\n")


def read_compressed_file(path: str) -> Tuple[Dict[str, int], str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if "===FREQ_MAP_JSON===" not in lines or "===DATA_BITS===" not in lines:
        raise ValueError("Invalid compressed file format.")

    i1 = lines.index("===FREQ_MAP_JSON===")
    i2 = lines.index("===DATA_BITS===")

    if i2 <= i1 + 1:
        raise ValueError("Compressed file missing frequency map JSON.")

    freq_map = json.loads(lines[i1 + 1])
    bits = "".join(lines[i2 + 1:]).strip()
    return freq_map, bits


def encode_main(input_path: str, output_path: str) -> None:
    text = read_text_file(input_path)

    print_input_set(text)

    freq_map = build_frequency_map(text)
    print_frequency_map(freq_map)

    root = build_huffman_tree(freq_map)
    codes = build_code_map(root)
    print_tree_codes(codes)

    bitstring = encode_text(text, codes)


    original_bits = len(text) * 8
    compressed_bits = len(bitstring)
    print("===== COMPRESSION REPORT =====")
    print("Original bits (estimated 8-bit/char):", original_bits)
    print("Compressed bits:", compressed_bits)
    if original_bits > 0:
        print("Compression ratio (compressed/original):", round(compressed_bits / original_bits, 4))
    print()

    write_compressed_file(output_path, freq_map, bitstring)
    print(f"Wrote compressed file to: {output_path}")


def decode_main(input_path: str, output_path: str) -> None:
    freq_map, bitstring = read_compressed_file(input_path)

    print("===== DECODE INPUT =====")
    print("Compressed file:", input_path)
    print("Unique chars in freq map:", len(freq_map))
    print("Bitstring length:", len(bitstring))
    print()

    root = build_huffman_tree(freq_map)
    text = decode_bits(bitstring, root)

    write_text_file(output_path, text)
    print(f"Wrote reconstructed document to: {output_path}")


def usage() -> None:
    print("Usage:")
    print("  py hw7_huffman.py encode <input.txt> <compressed.txt>")
    print("  py hw7_huffman.py decode <compressed.txt> <reconstructed.txt>")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)

    mode = sys.argv[1].lower()
    in_path = sys.argv[2]
    out_path = sys.argv[3]

    if mode == "encode":
        encode_main(in_path, out_path)
    elif mode == "decode":
        decode_main(in_path, out_path)
    else:
        usage()
        sys.exit(1)


# In[ ]:




