from package_utils.context.entry_point import create_entry_point

from webapp_starter.context import context
from webapp_starter.main.main import main

entry_point = create_entry_point(main, context)
