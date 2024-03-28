from typing import Any, Dict, List, Set


class CommandBase:
    @property
    def name(self) -> str:
        raise NotImplementedError()

    @property
    def invocation(self) -> str:
        raise NotImplementedError()

    def printHelp(self) -> None:
        print(f"Invoke {self.name} as: {self.invocation}")

    def run(self, args: List[str]) -> None:
        raise NotImplementedError()


class CommandRunner:
    def __init__(self, commands: Set[CommandBase]):
        self._commands = commands

    def printHelp(self):
        guide = "\n".join(
            list(
                map(
                    lambda command: command.invocation,
                    self._commands,
                ),
            ),
        )

        print(f"\n\nThe following commands are available:\n\n{guide}\n")

    def run(self, args):
        matchingCommand: CommandBase | None = None

        for command in self._commands:
            if command.name == args[0]:
                matchingCommand = command

                break

        if matchingCommand == None:
            self.printHelp()

            return

        matchingCommand.run(args[1:])


database: Dict[str, Any] = {
    "usernames": [],
    "advertisements": {},
}


class RegisterCommand(CommandBase):
    @property
    def name(self) -> str:
        return "register"

    @property
    def invocation(self) -> str:
        return "register <username>"

    def run(self, args) -> None:
        if len(args) != 1:
            self.printHelp()

            return

        username = args[0]
        usernames: List[str] = database["usernames"]

        if username in usernames:
            print("invalid username")

            return

        usernames.append(username)

        print("registered successfully")


class AddAdvertiseCommand(CommandBase):
    @property
    def name(self) -> str:
        return "add_advertise"

    @property
    def invocation(self) -> str:
        return "add_advertise <username> <title>"

    def run(self, args) -> None:
        if len(args) != 2:
            self.printHelp()

            return

        username, title = args
        usernames: List[str] = database["usernames"]
        advertisements: Dict[str, str] = database["advertisements"]

        if username not in usernames:
            print("invalid username")

            return

        if title in advertisements.keys():
            print("invalid title")

            return

        advertisements[title] = username

        print("posted successfully")


class RemAdvertiseCommand(CommandBase):
    @property
    def name(self) -> str:
        return "rem_advertise"

    @property
    def invocation(self) -> str:
        return "rem_advertise <username> <title>"

    def run(self, args) -> None:
        if len(args) != 2:
            self.printHelp()

            return

        username, title = args
        usernames: List[str] = database["usernames"]
        advertisements: Dict[str, str] = database["advertisements"]

        if username not in usernames:
            print("invalid username")

            return

        if title not in advertisements.keys():
            print("invalid title")

            return

        if advertisements[title] != username:
            print("access denied")

            return

        del advertisements[title]

        print("removed successfully")


class ListMyAdvertisesCommand(CommandBase):
    @property
    def name(self) -> str:
        return "list_my_advertises"

    @property
    def invocation(self) -> str:
        return "list_my_advertises <username>"

    def run(self, args) -> None:
        if len(args) != 1:
            self.printHelp()

            return

        username = args[0]
        usernames: List[str] = database["usernames"]
        advertisements: Dict[str, str] = database["advertisements"]

        if username not in usernames:
            print("invalid username")

            return

        listing = [
            title
            for title, _username in advertisements.items()
            if _username == username
        ]

        print(" ".join(listing))


commandRunner = CommandRunner(
    commands={
        RegisterCommand(),
        AddAdvertiseCommand(),
        RemAdvertiseCommand(),
        ListMyAdvertisesCommand(),
    }
)

numberOfCommands = int(input())

commandsArgs: List[List[str]] = []

for _ in range(numberOfCommands):
    args = input().split(" ")

    commandsArgs.append(args)


for args in commandsArgs:
    commandRunner.run(args)
