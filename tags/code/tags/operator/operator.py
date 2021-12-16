from talon import Module, Context
from user.core import csv

mod = Module()
mod.tag("code_operator", desc="Tag which provides a general list for operators")
mod.list("code_operator", desc="List of operators")

