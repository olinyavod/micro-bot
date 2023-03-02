import sys
import uasyncio as asyncio


class AConsole:
    def __init__(self, s_in=sys.stdin, s_out=sys.stdout):
        self._reader = asyncio.StreamReader(s_in)
        self._writer = asyncio.StreamWriter(s_out, {})

    async def input(self, prompt='', password=False) -> str:
        await self._writer.awrite(prompt)
        result = ""

        while True:
            c = await self._reader.read(1)
            n = ord(c)

            if n == 9:  # Tab
                pass
            elif n == 10:  # Enter
                if await self._reader.read(1) == '\n':
                    break
            elif n == 8 and len(result) > 0:  # Del
                if not password:
                    await self._writer.awrite(f"{c} {c}")
                result = result[0:len(result)-1]
                pass
            # elif n == 32: # Space
            #    pass
            elif n == 26:  # ^Z
                pass
            elif n == 24:  # ^X
                pass
            elif n == 22:  # ^V
                pass
            elif n == 2:  # ^B
                pass
            elif n == 1:  # ^A
                pass
            elif n == 19:  # ^S
                pass
            elif n == 7:  # ^G
                pass
            elif n == 8:  # ^H
                pass
            elif n == 11:  # ^K
                pass
            elif n == 12:  # ^L
                pass
            else:
                result += c
                if not password:
                    await self._writer.awrite(c)

        await self._writer.awrite("\n\r")
        return result
