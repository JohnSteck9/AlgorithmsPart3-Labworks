# Robin-Karp algorithm
# max complexity = O(n)

class RabinCarp:
    def __init__(self, text, pattern_len):
        self.text = text
        self.pattern_len = pattern_len
        self.base = 256
        self.window_start = 0
        self.window_end = 0
        # Mersen number for machine
        # 64bit  = (2 ** 64) - 1 | 32bit = (2**32) - 1
        self.mod = (2 ** 64) - 1
        self.base_char = 0  # ord first char
        self.hash = self.get_hash(text, pattern_len)

    def get_hash(self, text, pattern_len):
        base_char = 0
        hash_value = 0
        for i in range(0, pattern_len):
            hash_value += (ord(self.text[i]) - base_char) * (self.base ** (pattern_len - i - 1)) % self.mod

        self.window_start = 0
        self.window_end = pattern_len

        return hash_value

    def next_window(self):
        if self.window_end <= len(self.text) - 1:
            new_hash = (self.hash -
                        (ord(self.text[self.window_start]) - 0) * self.base ** (self.pattern_len - 1)) \
                       * self.base \
                       + ord(self.text[self.window_end]) - 0 \
                       % self.mod

            self.hash = new_hash
            self.window_start += 1
            self.window_end += 1
            return True
        return False

    def current_window_text(self):
        return self.text[self.window_start:self.window_end]


def main(text, pattern):
    if text == "" or pattern == "":
        return None
    if len(pattern) > len(pattern):
        return None

    text_rolling = RabinCarp(text, len(pattern))
    pattern_rolling = RabinCarp(pattern, len(pattern))

    for i in range(len(text) - len(pattern) + 1):
        # print(text_rolling.hash)
        # print(pattern_rolling.hash)
        if text_rolling.hash == pattern_rolling.hash:
            if final_check(text[i:i], pattern):
                print(1)
                continue
            return True
            # return f"Found {i}...{i + len(pattern)}"
        text_rolling.next_window()
    return False
    # return "Not Found"


# Las Vegas version
def final_check(str1, str2):
    return True if str1 == str2 else False


if __name__ == "__main__":
    print(main("abcdfAghdeккAКefDeffl", "ккК"))
    # print(ord('A'))
