import nuke
import autoBackup

nuke.menu("Nuke").addCommand("utilities/autoBackup/open backup directory", "autoBackup.open_backup_dir()")
nuke.addOnScriptSave(autoBackup.make_backup)
