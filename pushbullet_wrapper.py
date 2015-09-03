#!/usr/bin/env python
import sys
import click
import datetime

from pushbullet import Pushbullet


@click.command()
# The PushbulletAPI key you want to use
@click.argument("api_key", required=True)
@click.option("--tock", help="The tock notification you want to show. Use " +
              "this to show the tock notification instead of manually " +
              "passing in a title and a message.")
@click.option("--title", help="The title of the pushbullet note to show.")
@click.option("--message", help="The message of the pushbullet note to show.")
def main(api_key, tock, title, message):
    pb = Pushbullet(api_key)
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
    elif title and message:
        pb.push_note(title, message)
    else:
        raise Exception("Unrecognized command.")

if __name__ == '__main__':
    main()
