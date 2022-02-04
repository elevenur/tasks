#!usr/bin/env python3
import os.path
import argparse
import json

storageFilepath = './storage.data'

try:
  parser = argparse.ArgumentParser()
  parser.add_argument('--key', type = str)
  parser.add_argument('--val', type = str)

  args = parser.parse_args()

  if os.path.isfile(storageFilepath):
   
    with open(storageFilepath, 'r') as storage:
      try:
        recordsList = json.load(storage)
      except:
       
        recordsList = []
  else:
  
    open(storageFilepath, 'w', encoding = 'utf-8').close()
    recordsList = []

  if args.key and args.val:
 
    recordsList.append({
      'key': args.key,
      'val': args.val
    })
    with open(storageFilepath, 'w', encoding = 'utf-8')  as storage:
      json.dump(recordsList, storage, indent = 2)

  elif args.key:
   
    values = [record['val'] for record in recordsList if record['key'] == args.key]
    print(','.join(values))

  else:
    print('Не передны аргументы key и val!')

except:
  print('Возникла непредвиденная ошибка')
