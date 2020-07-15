
import os


class fileExplorer():
    def __init__(self):
        pass

    def find_files(self, suffix, path):
        """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system

        Returns:
        a list of paths
        """
        if (suffix is None or path is None or path == '' or suffix == ''):
            return None

        file_list = None
        file_list = self.search_in_dir(suffix, path, [])
        return file_list

    def search_in_dir(self, suffix, path, file_list):
        """
        Search the files for the given suffix within the folder (path)
        add the fils in the input file_list

        for each folder search again with the same function

        Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system
        file_list(array): the array to append files that are found

        Returns:
        a list of paths
        """
        if os.path.exists(path) and os.path.isfile(path):
            if path.endswith(suffix):
                return [path]
            else:
                return []

        try:
            directory_list = os.listdir(path)
        except FileNotFoundError as error:
            print(error)
            return

        sub_dirs = []
        for item in directory_list:
            if os.path.isfile(path+"/"+item):
                if item.endswith(suffix):
                    file_list.append(path+"/"+item)
            elif os.path.isdir(path+"/"+item):
                self.search_in_dir(suffix, path+"/"+item, file_list)

        return file_list


if __name__ == "__main__":
    print("Tests start looking for subdirectory 'testdir' under the script-running directory")
    print("testing for testdir and files .c")
    file_explorer = fileExplorer()

    assert file_explorer.find_files('.c', 'testdir') == \
        ['testdir/subdir1/a.c', 'testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c',
            'testdir/t1.c'],  f" files: .c"

    print("testing for testdir and files .h")
    assert file_explorer.find_files('.h', 'testdir') == \
        ['testdir/subdir1/a.h', 'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h',
            'testdir/t1.h'],  f" files: .h"

    print("testing for testdir and files .a to be none")
    assert file_explorer.find_files('.', 'testdir') == \
        [],  f" files: .h"

    print("testing for testdir and empty suffix")
    assert file_explorer.find_files('', 'testdir') == \
        None,  f" files: ''"

    print("testing for testdir and no suffix")
    assert file_explorer.find_files(None, 'testdir') == \
        None,  f" files: ''"
    print("testing for empty folder and .c suffix")
    assert file_explorer.find_files('.c', '') == \
        None,  f" files: ''"

    print("testing for None folder and .c suffix")
    assert file_explorer.find_files('.c', None) == \
        None,  f" files: ''"

    print("testing directory to be a valid file to return")
    path = "testdir/subdir3/subsubdir1/b.h"
    suffix = ".h"
    assert file_explorer.find_files(suffix, path) == [
        "testdir/subdir3/subsubdir1/b.h"], f"direct file found"

    print("testing directory to be file but not valid for our search")
    path = "testdir/subdir3/subsubdir1/b.h"
    suffix = ".c"
    assert file_explorer.find_files(
        suffix, path) == [], f"direct file missing suffix"
    print("all passed")
