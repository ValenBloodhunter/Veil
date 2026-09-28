import pickle
import pandas

from flask import request, jsonify

LOCAL_CACHE = {}