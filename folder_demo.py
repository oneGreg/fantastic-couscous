#
# 'INBOX|folder1'
def createFolder(mailbox, folderString):
    if(mailbox.folder.exists(folderString)):
      mailbox.folder.create('INBOX|folder1')

def printFolderTree(folder):
  for subFolder in folder.list:
    print('folder.name:' + subFolder.name)
    printFolderTree(subFolder)
