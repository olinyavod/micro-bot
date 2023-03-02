import pyb

import uasyncio as asyncio

from robot import Robot
from term import AConsole


async def command_process(robot: Robot) -> None:
    term = AConsole()
    while True:
        cmd = await term.input("robot> ")

        if cmd == "quit":
            return
        elif cmd == "distance":
            print(f"Distance: {robot.distance():.2f} cm")


def main():
    robot = Robot()

    loop = asyncio.get_event_loop()

    loop.create_task(command_process(robot))
    loop.create_task(robot.run())

    loop.run_forever()


if __name__ == '__main__':
    pyb.wfi()
    main()

