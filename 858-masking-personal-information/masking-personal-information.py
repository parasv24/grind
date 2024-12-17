class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.split("@")
            name = name.lower()
            domain = domain.lower()
            return name[0] + "*****" +name[-1] + "@" +domain
        else:
            digits = [ch for ch in s if ch.isdigit()]
            part_last = "***-***-" + "".join(digits[-4:])
            if len(digits) == 10:
                return part_last
            else:
                return "+" + (len(digits) - 10) * "*" + "-" + part_last
        