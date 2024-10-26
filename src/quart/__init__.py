from __future__ import annotations

from markupsafe import escape, Markup

from .app import Quart
from .blueprints import Blueprint
from .config import Config
from .ctx import (
    after_this_request,
    copy_current_app_context,
    copy_current_request_context,
    copy_current_websocket_context,
    has_app_context,
    has_request_context,
    has_websocket_context,
)
from .globals import (
    current_app,
    g,
    request,
    session,
    websocket,
)
from .helpers import (
    abort,
    flash,
    get_flashed_messages,
    get_template_attribute,
    make_push_promise,
    make_response,
    redirect,
    send_file,
    send_from_directory,
    stream_with_context,
    url_for,
)
from .json import jsonify
from .signals import (
    appcontext_popped,
    appcontext_pushed,
    appcontext_tearing_down,
    before_render_template,
    got_request_exception,
    got_websocket_exception,
    message_flashed,
    request_finished,
    request_started,
    request_tearing_down,
    signals_available,
    template_rendered,
    websocket_finished,
    websocket_started,
    websocket_tearing_down,
)
from .templating import (
    render_template,
    render_template_string,
    stream_template,
    stream_template_string,
)
from .typing import ResponseReturnValue
from .wrappers import Request, Response, Websocket
