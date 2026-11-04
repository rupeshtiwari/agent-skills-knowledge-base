#!/usr/bin/env python3
"""Build once, then serve only generated public files on localhost."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from build_site import build


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--host', default='127.0.0.1')
    args = parser.parse_args()
    directory = build()
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    try:
        with ThreadingHTTPServer((args.host, args.port), handler) as server:
            print(f'Open http://{args.host}:{server.server_port}/ — Ctrl+C to stop', flush=True)
            server.serve_forever()
    except KeyboardInterrupt:
        pass
    except OSError as error:
        parser.exit(1, f'Cannot start server: {error}. Try --port 8001.\n')


if __name__ == '__main__': main()
