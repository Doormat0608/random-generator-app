import json

def load_config(config_file):
    if config_file is not None:
        try:
            return json.load(config_file)
        except Exception:
            return {}
    return {}

def save_config_json(a1, b1, a2, b2, xmin, xmax, w, N):
    settings = {
        'a1': a1,
        'b1': b1,
        'a2': a2,
        'b2': b2,
        'xmin': xmin,
        'xmax': xmax,
        'w': w,
        'N': int(N)
    }
    return json.dumps(settings, ensure_ascii=False, indent=4)
