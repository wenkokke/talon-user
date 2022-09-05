from talon import Context, Module, ui

from user.util.speech import create_spoken_forms_app

mod = Module()
ctx = Context()

# List of running applications in the Talon scope:


@mod.scope
def scope():
    return {"running": {app.name.lower() for app in ui.apps()}}


ui.register("app_launch", scope.update)
ui.register("app_close", scope.update)


# List of running applications in a Talon list

mod.list("running", desc="All running applications")

RUNNING_APPLICATION_DICT = {}


def update_running_list():
    global RUNNING_APPLICATION_DICT
    running = {}
    for cur_app in ui.apps(background=False):
        RUNNING_APPLICATION_DICT[cur_app.name] = True
        for spoken_form in create_spoken_forms_app(cur_app.name):
            running[spoken_form] = cur_app.name

    # batch update lists
    ctx.lists.update(
        {
            "self.running": running,
        }
    )


ui.register("app_launch", lambda evt: update_running_list())
ui.register("app_close", lambda evt: update_running_list())
