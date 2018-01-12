import shutil
import os
import baker

def folder_check(folder_path):
    if folder_path[-1]!='/':
        folder_path += '/'
    return folder_path
@baker.command
def copyfile(txt_folder, alljpg_folder, somejpg_folder, list_folder):
    txt_folder     = folder_check(txt_folder)
    alljpg_folder  = folder_check(alljpg_folder)
    somejpg_folder = folder_check(somejpg_folder)
    list_folder    = folder_check(list_folder)
    # Create a new folder for storing copied jpgs
    if not os.path.exists(somejpg_folder):
        os.makedirs(somejpg_folder)
        print('Create a new folder as somejpg_folder: {}'.format(somejpg_folder))
    # Demonstrate how many jpgs needed to be applied
    txt_ids = os.listdir(txt_folder)
    print('{} jpgs need to be copied!'.format(len(txt_ids)))
    # Do iteration for copying jpgs and record jpg_path
    print('Looking for jpgs in: {}'.format(alljpg_folder))
    if not os.path.exists(list_folder):
        os.makedirs(list_folder)
        print('Create a new folder for storing list.txt at: {}'.format(list_folder))
    list_file = open(list_folder+'jpg_path_list.txt','w')
    for ct, txt_id in enumerate(txt_ids):
        ct+=1
        if ct%500==0:
            print('Already copied {} jpgs!'.format(ct))
        jpg_id = txt_id.replace('txt','jpg')
        shutil.copy(alljpg_folder+jpg_id,somejpg_folder+jpg_id)
        # Write jpg_path list.txt
        list_file.write(somejpg_folder+jpg_id+'\n')
    print('Done!\nSuccessfully copied {} jpgs!'.format(ct))
    
@baker.command
def write_list(somejpg_folder, list_folder):
    somejpg_folder = folder_check(os.path.abspath(somejpg_folder))
    list_folder    = folder_check(list_folder)
    if not os.path.exists(list_folder):
        os.makedirs(list_folder)
        print('Create a new folder for storing list.txt at: {}'.format(list_folder))
    list_file = open(list_folder+'jpg_path_list.txt','w')
    for ct, img_id in enumerate(os.listdir(somejpg_folder)):
        list_file.write(somejpg_folder+img_id+'\n')
    print('Done!\nSuccessfully record {} jpg-paths!'.format(ct+1))    
    list_file.close()

if __name__ == '__main__':
    baker.run()
