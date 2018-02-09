import nuke
import os, sys, time
import helper

backup_dir = "{}/nuke_backups".format(os.path.expanduser("~"))
number_of_backups = 5

def get_script_name():
    script = nuke.root().name()
    script_name = os.path.basename(script)
    script_name = os.path.splitext(script_name)[0]

    return script_name

def open_backup_dir():
    script_name = get_script_name()
    script_backup_dir = "{}/{}".format(backup_dir, script_name)
    helper.open_foloder(script_backup_dir)

def make_backup():
    script_name = get_script_name()
    script_backup_dir = "{}/{}".format(backup_dir, script_name)
    current_time = time.strftime("%y%m%d-%H%M")

    if not os.path.isdir(script_backup_dir):
        os.makedirs(script_backup_dir)

    try:
        nuke.removeOnScriptSave(make_backup)
        nuke.scriptSave("{}/backup_{}_{}.nk".format(script_backup_dir, current_time, script_name))
        nuke.addOnScriptSave(make_backup)
    except:
        nuke.message("Could't write a backup file!!")

    delete_older_backup_versions(script_backup_dir)

def delete_older_backup_versions(path):
    files_list = []
    keep_list = []

    for filename in os.listdir(path):
        if os.path.splitext(filename)[1] == ".nk"
            files_list.append(filename)

    if len(files_list) > number_of_backups:
        keep_list = files_list[-number_of_backups:]

    for filename in files_list:
        if filename not in keep_list:
            file_to_delete = "{}/{}".format(path, filename)
            if os.path.isfile(file_to_delete):
                os.remove(file_to_delete)
