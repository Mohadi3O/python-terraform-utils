def main():
    from terraform_model.cli.root import parser_root

    args = parser_root.parse_args()

    # set log level
    from terraform_model.utils import log
    log.set_verbosity(args.v)
    if args.info:
        log.set_level('info')
    if args.verbose:
        log.set_level('verbose')
    if args.debug:
        log.set_level('debug')
    if args.trace:
        log.set_level('trace')
    if args.silly:
        log.set_level('silly')

    args.func(args)


if __name__ == '__main__':
    main()
