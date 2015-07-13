#!/usr/bin/python
import sys
for p in sys.path:
    print p
import click
import datetime

# TODO: move the API key for this somewhere safe so i can version control this
# file
from pushbullet import Pushbullet
pb = Pushbullet("v1oZ3Cg4FfihCR0U1mWYR49kkxhFMpQqxUujA49u7oU20")


@click.command()
@click.option("--tock", help="The tock notification you want to show. Use " +
              "this to show the tock notification instead of manually " +
              "passing in a title and a msg.")
@click.option("--title", help="The title of the pushbullet note to show.")
@click.option("--message", help="The message of the pushbullet note to show.")
def main(tock, title, msg):
    if tock:
        now_dt = datetime.datetime.now()
        now_dt_str = now_dt.strftime("%H:%M")
        # TODO: Move the tock sounds to this function as well
        if tock == "tock_start":
            pb.push_note("Tock starting!", "Tock starting at %s" % now_dt_str)
        elif tock == "tock_done":
            pb.push_note("Tock done!", "Tock done at %s" % now_dt_str)
        elif tock == "break_done":
            pb.push_note("Break done!", "Break done at %s" % now_dt_str)
    elif title and msg:
        pb.push_note(title, msg)
    else:
        raise Exception("Unrecognized command.")

if __name__ == '__main__':
    main()
