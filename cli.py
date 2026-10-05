from MEISTERMASCHINE.__main__ import main

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3 and sys.argv[1] == '--smoke-test':
        from MEISTERMASCHINE.packaging_check import run
        sys.exit(run(sys.argv[2]))
    main()
