import select
import sys
import uasyncio as asyncio


class AsyncTerm:
    def __init__(self):
        self._poller = select.poll()
        self._poller.register(sys.stdin, select.POLLIN)

    def get_char(self):
        for s, ev in self._poller.poll(500):
            return s.read(1)

    async def input(self, prompt=''):
        result = ''
        while True:
            c = self.get_char()
            if (c):
                if ord(c) == 10: # enter
                    print()
                    return result
                elif ord(c) == 27: # esc
                    return ''
                elif ord(c) == 127: # bs
                    result = result[:-1]
                else:
                    result += c
                sys.stdout.write("%s%s   \r" % (prompt, result))
            await asyncio.sleep(0.2)