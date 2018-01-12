import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir
from os.path import join
import baker

#classes = ['bowl']
#classes = ['banana']
#xml_folder = '/home/kris/github/coco2pascal2txt/xmls/'

def exist_a_class(xml_path,classes):
    in_file = open(xml_path,'r')
    tree=ET.parse(in_file)
    root = tree.getroot()
    existance = False
    for obj in root.iter('object'):
        if obj.find('difficult')==None:
            difficult = 0
        else:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        existance = True
    in_file.close()
    return existance

@baker.command
def calculate(cls_str, xml_folder):
    classes = [cls_str]
    print('Start Counting {}!'.format(classes[0]))
    print('Read xml files in xml_folder: {}'.format(xml_folder))
    count = 0
    for ct, xml_id in enumerate(os.listdir(xml_folder)):
        if ((ct+1)%5000)==0 and ct!=0:
            print('Already loaded {} xml files!'.format(ct+1))
        # Count a class
        if exist_a_class(xml_folder+xml_id,classes):
            count+=1
    print('Finally loaded {} xml files'.format(ct+1))
    print('There exists {} {}s !!'.format(count,classes[0]))
    
if __name__ == '__main__':
    baker.run()