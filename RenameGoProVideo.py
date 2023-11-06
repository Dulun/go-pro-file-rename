import os

from datetime import datetime




def rename_gopro_all():
# Use a breakpoint in the code line below to debug your script.
  path = "./"
  count = 0
  file_list = os.listdir(path)
  print (file_list)
  for file in file_list:
    olddir = os.path.join(path,file)
    if os.path.isdir(olddir):
      continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1].upper()


    # ctime = os.path.getctime(file) #创建时间
    # ctime_string = datetime.fromtimestamp(int(ctime))

    # mtime = os.path.getmtime(file) #修改时间
    # mtime_string = datetime.fromtimestamp(int(ctime))

    # atime = os.path.getatime(file) #修改时间
    # atime_string = datetime.fromtimestamp(int(ctime))

    # stinfo = os.stat(file)

    # datetime.fromtimestamp(int(stinfo.st_ctime))

    # print(stinfo)

    # print(
    #   f"创建时间：{ctime_string}", 
    #   f"修改时间：{mtime_string}", 
    #   f"访问时间：{atime_string}", 
    #   f"文件大小：{stinfo.st_size}字节",
    #   f"文件权限：{stinfo.st_mode}",
    #   f"文件所有者：{stinfo.st_uid}",
    #   f"文件所有者所在组：{stinfo.st_gid}",

    #   f"文件最近访问时间：{datetime.fromtimestamp(int(stinfo.st_atime))}",
    #   f"文件最近修改时间：{datetime.fromtimestamp(int(stinfo.st_mtime))}",
    #   # f"文件创建时间：{datetime(stinfo.st_ctime.strftime).('%Y-%m-%d %H:%M:%S')}",
    #   f"文件创建时间：{(datetime.fromtimestamp(stinfo.st_mtime)).strftime('%y-%m-%dT%H:%M')}",

    #   sep="\n"
    # )

    # stinfo = os.stat(file)

    prefixDateTimeFileName = (datetime.fromtimestamp(os.stat(file).st_mtime)).strftime('%y-%m-%dT%H-%M')

    print(prefixDateTimeFileName)
    print ("Filename =", filename)
    print ("FileTYpe =", filetype)
    # if filetype in [".MP4",".JPG",".LRV",".THM"] and filename[0]=="G" and "_" not in filename:
    if filetype in [".MP4",".JPG",".LRV",".THM"]:
      NAME_PREFIX = filename[:2]
      NAME_INDEX = filename[2:4]
      NAME_SEQ = filename[4:]
      print ("Name_Prefix=", NAME_PREFIX)
      print ("Name Index =", NAME_INDEX)
      print ("Name Seq =", NAME_SEQ)

      # newdir = os.path.join(path, prefixDateTimeFileName + NAME_PREFIX + NAME_SEQ + "_" + NAME_INDEX + filetype.lower())
      newdir = os.path.join(path, NAME_PREFIX + NAME_SEQ +  "_" + prefixDateTimeFileName + filetype.lower())
      print (newdir)
      os.rename(olddir,newdir)
      count +=1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  rename_gopro_all ()




