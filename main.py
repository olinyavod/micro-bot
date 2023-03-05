import pyb

import uasyncio as asyncio

from robot import Robot
from lib.term import AConsole
from machine import UART
from micropython import const, alloc_emergency_exception_buf


async def command_process(term: AConsole, robot: Robot) -> None:
    while True:
        await term.print("robot> ")
        cmd = await term.readline()
        l = len(cmd)
        cmd = cmd[0:l - 2] if l > 2 else cmd

        if cmd == b'quit' or cmd == b'q':
            raise KeyboardInterrupt
        elif cmd == b'distance' or cmd == b'dist':
            await term.print(f"Distance: {robot.distance():.2f} cm")
        else:
            print(cmd)


async def run(robot, term):
    await asyncio.gather(asyncio.create_task(command_process(term, robot)), asyncio.create_task(robot.run()))


def main():
    is_continue = False
    robot = Robot()
    uart = UART(2, 9600)
    uart.init(9600, bits=8, parity=None, stop=1)

    term = AConsole(uart, uart)
    try:
        asyncio.run(run(robot, term))
    except KeyboardInterrupt:
        pyb.wfi()
        is_continue = input("Robot interrupted. Continue? y/n: ") == "y"
    finally:
        robot.close()
        term.close()
        uart.deinit()
        asyncio.new_event_loop()
        if is_continue:
            main()


if __name__ == '__main__':
    alloc_emergency_exception_buf(250)
    main()
