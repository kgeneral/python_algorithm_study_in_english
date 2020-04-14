class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) > 1:
            chars.append("!")

            count=1
            prev=chars[0]

            idx = 0
            for i, c in enumerate(chars):
                if i==0:
                    continue

                if c == prev:
                    count += 1
                else:
                    chars[idx] = prev
                    idx += 1
                    if count > 1:
                        for digit in str(count):
                            chars[idx] = digit
                            idx += 1

                    prev = c
                    count=1


            chars = chars[:idx]
        
        return len(chars)
