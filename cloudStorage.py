import dropbox

class TransferData:
    def __init__ (self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AuvTya4bfsHN9epJIJMQT5MHZv5mznCI4_duQUXz7OC6pH6ZEjNacQtuFxRcd2_En1iOwbyY7QfcsuPap3BpZ4ArCM36XZUIqBtpRl2Lkf6KHsvIKklHlEFGeCWHCM70HEeOm84'
    transferData=TransferData(access_token)

    file_from = input("enter file path to transfer : ")
    file_to =input("enter the full path to upload to dropbox : ")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()