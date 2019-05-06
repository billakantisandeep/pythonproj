def _parse_args(args):
    parser = argparse.ArgumentParser()

    if any([arg == '--version' for arg in args]):
        return argparse.Namespace(version=True)

    parser.add_argument('script', help='Script to run')
    parser.add_argument('target', nargs='?', default='build', help='Target object to build; defaults to \'build\'')
    parser.add_argument('--version', action='store_true', help='Print the version and exit')
    parser.add_argument('--clear', action='store_true', help='Clear output directory')
    parser.add_argument('--clear-cache', action='store_true', help='Clear cache before compiling')
    parser.add_argument('--threads', '-t', type=int, help='Set thread count; defaults to cores*2')
    paser.add_argument('--no-threading', '-nt', action='store_true', help='Disable multithreaded compilation')

    return parser.parse_args(args)

    