import nuke
import glob
import time
import os


def onAutoSave(filename):
    if nuke.root().name() == 'Root':
        return filename

    fileNo = 0
    files = getAutoSaveFiles(filename)

    if len(files) > 0:
        lastFile = files[-1]

    if len(lastFile) > 0:
        try:
            fileNo = int(lastFile[-1:])
        except:
            pass

        fileNo = fileNo + 1

    if (fileNo > 9):
        fileNo = 0

    if (fileNo != 0):
        filename = filename + str(fileNo)

    return filename


def onAutoSaveRestore(filename):
    files = getAutoSaveFiles(filename)

    if len(files) > 0:
        filename = files[-1]

    return filename


def onAutoSaveDelete(filename):
    if nuke.root().name() == 'Root':
        return filename

    return None


def getAutoSaveFiles(filename):
    date_file_list = []
    files = glob.glob(filename + '[1-9]')
    files.extend(glob.glob(filename))

    for file in files:
        stats = os.stat(file)
        lastmod_date = time.localtime(stats[8])
        date_file_tuple = lastmod_date, file
        date_file_list.append(date_file_tuple)

    date_file_list.sort()

    return [filename for _, filename in date_file_list]


nuke.addAutoSaveFilter(onAutoSave)
nuke.addAutoSaveRestoreFilter(onAutoSaveRestore)
nuke.addAutoSaveDeleteFilter(onAutoSaveDelete)

# As an example to remove the callbacks use this code
# nuke.removeAutoSaveFilter(onAutoSave)
# nuke.removeAutoSaveRestoreFilter(onAutoSaveRestore)
# nuke.removeAutoSaveDeleteFilter(onAutoSaveDelete)
