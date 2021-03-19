import argparse
import os
from collections import defaultdict
import subprocess

BLOCK_SIZE = 1024


class PlushkinsHelper:
    """Find and delete all duplicates in folder.

        Args:
            path (str): path to folder, there should find duplicates.
            delete: Use this flag to delete duplicates.
                Don`t use to view duplicates.

        Returns:
            None

    """

    def __init__(self, path, delete=False):
        self.delete = delete
        self.path = path
        self.unique = dict()
        self.not_unique = defaultdict(list)
        self.files_scanned = int()
        self.folders_scanned = int()
        self.duplications_count = int()
        self.files_removed = 0
        self.remove_error = 0
        self.all_size = 0

    def run(self):
        """Start script.

        The function calls the main functions in order.
        If script has no "--delete" key or duplications not found,
        just print information about it and exit.

        """
        self.find_all_duplicates()
        self.print_start_info()
        if not self.delete or not self.not_unique:
            self.print_all_duplicates()
            exit()
        self.prepare_to_delete()
        self.print_ends_info()

    @staticmethod
    def read_hash(filename):
        """Reads a file and returns hash.

        Args:
            filename (str): full path to file.

        Returns
            str: hash of file.

        """
        checksum_process = subprocess.run(
            ["md5sum", filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        return checksum_process.stdout.split()[0]

    def find_all_duplicates(self):
        """Find all duplicates and write them to "not_unique" dict.
        All unique files saves to "unique" dict.
        """
        for dirname, _, filenames in os.walk(self.path):
            self.folders_scanned += 1
            for filename in filenames:
                self.files_scanned += 1
                full_path = os.path.join(dirname, filename)
                filehash = self.read_hash(full_path)
                if filehash in (*self.unique, *self.not_unique):
                    self.not_unique[filehash].append(full_path)
                    self.duplications_count += 1
                    if filehash in self.unique:
                        self.not_unique[filehash].append(self.unique[filehash])
                        del self.unique[filehash]
                else:
                    self.unique[filehash] = full_path

    def print_start_info(self):
        """Print start info."""
        print(f'Scan report for folder: {self.path}\n'
              f'Files scanned: {self.files_scanned}\n'
              f'Folders scanned: {self.folders_scanned}\n'
              f'Duplications found: {self.duplications_count}\n'
              ''.rjust(50, '-'))

    def print_ends_info(self):
        """Print ends info."""
        print(''.rjust(50, '-'),
              '\nCLEANING finished\n'
              ''.rjust(50, '-'),
              f'\nFiles removed: {self.files_removed}\n'
              f'Errors: {self.remove_error}\n'
              f'Size cleaned: {self.all_size}\n')

    def print_all_duplicates(self):
        """If --delete flag was not used, print all duplicates by groups."""
        for i, item in enumerate(self.not_unique.values(), 1):
            print(f'[Group {i}]: {item}')

    def prepare_to_delete(self):
        """If --delete flag was used, print duplicates and start deleting."""
        print('CLEANING started')
        print(''.rjust(50, '-'))
        for duplicates in self.not_unique.values():
            for i, item in enumerate(duplicates, 1):
                print(f'[{i}]: {item}')
            self.delete_duplicates(duplicates)

    @staticmethod
    def wait_for_input(duplicates):
        """Expects from the user what file to leave on the system.

        If input invalid, print info about it.

        Args:
            duplicates (list): List with duplicates of group.

        Returns:
            number (int): Number from input.

        """
        while True:
            number = input('Choose file to keep by entering its number '
                           'or press enter to skip it\n')
            try:
                number = int(number)
                if number > len(duplicates) or number <= 0:
                    print('Incorrect number.')
                    continue
                return number
            except ValueError:
                if not number:
                    return False
                print('Invalid value entered.')

    def delete_duplicates(self, duplicates):
        """Delete duplicates except one from input."""
        number = self.wait_for_input(duplicates)
        if not number:
            return
        for i, file in enumerate(duplicates, 1):
            if i != number:
                try:
                    self.all_size += os.stat(file).st_size
                    os.remove(file)
                    self.files_removed += 1
                except PermissionError as exc:
                    self.remove_error += 1
                    print(exc)
            else:
                print(f'{file} was kept.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find and delete duplicates in folder')
    parser.add_argument(
        '--delete',
        help='Pass this flag to delete duplicates',
        action='store_true',
        required=False
    )
    parser.add_argument('path', type=str, help='Path to folder')
    args = vars(parser.parse_args())

    PlushkinsHelper(**args).run()
