
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
        if (suffix is None or path is None):
            return None

        file_list = None
        file_list = self.search_in_dir(suffix, path, [])
        return file_list

    def search_in_dir(self, suffix, path, file_list):
        try:
            directory_list = os.listdir(path)
        except FileNotFoundError as error:
            print(error)
            return

        # print(directory_list)
        sub_dirs = []
        for item in directory_list:
            # item = path+"/"+item
            # print("processing> {}".format(item))
            if os.path.isfile(path+"/"+item):
                # print("found file {}".format(path+"/"+item))
                if item.endswith(suffix):
                    # print("added")
                    file_list.append(path+"/"+item)
            elif os.path.isdir(path+"/"+item):
                # print("found folder {}".format(path+"/"+item))
                sub_dirs.append(path+"/"+item)
        # print("files up to here: {}".format(file_list))
        # print("folders up to here: {}".format(sub_dirs))
        for sub_dir in sub_dirs:
            # print('going in subdir: {}'.format(sub_dir))
            sub_files = self.search_in_dir(suffix, sub_dir, file_list)
            # print("after recurse:{}".format(sub_files))
            # for sub_file in sub_files:
            #     file_list.append(sub_file)

        return file_list


file_explorer = fileExplorer()
print("c files: {}".format(file_explorer.find_files(".c", "testdir")))
