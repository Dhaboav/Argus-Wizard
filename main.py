import utils
import argparse


VERSION = "0.1.90"
PROGRAM_NAME = "MusicInfo"
DESCRIPTION = "To get artist name and music title"
EPILOG = "That's all of option :)"


def parse_arguments():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description=DESCRIPTION,
        epilog=EPILOG,
        formatter_class=argparse.MetavarTypeHelpFormatter
    )

    parser.add_argument('--version', action='version',
                        version=f'%(prog)s {VERSION}')
    parser.add_argument('-f', '--folder', type=str,
                        required=True, help='Folder that contains music')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file path (txt), default is output.txt')

    return parser.parse_args()


def main():
    """
    Main function to run the script.
    """
    args = parse_arguments()

    mp3_files = utils.list_files_in_folder(args.folder, '.mp3')
    if not mp3_files:
        print(f"No MP3 files found in the folder: {args.folder}")
        return

    results = [utils.handle_filename(file) for file in mp3_files]
    output_path = args.output if args.output else "output.txt"
    utils.write_to_file(output_path, results)


if __name__ == "__main__":
    main()
