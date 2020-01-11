
import os
import requests
import sys
import urllib
################
putih = '\033[37m'###
hijau = '\033[32m'###
merah = '\033[31m'##
kuning = '\033[33m'##
biru = '\033[34m'####
cyan = '\033[36m'###
################
api_url = "http://tinyurl.com/api-create.php"
class short:
         def main(self,url):
                 try:
                         get = api_url+ "?" \
                               +urllib.parse.urlencode({"url": url})
                         req = requests.get(get)


                         if "Error" in req.text:
                                 os.system('clear')
                                 print ('\033[31m╔═════════════════════════════════════════╗')
                                 print ("\033[31m|\033[36m [\033[31m!\033[37m] URL SALAH!: "+url)
                                 print ('\033[31m╚═════════════════════════════════════════╝')
                                 sys.exit()
                         else:
                                 os.system('clear')
                                 os.system('sh b.sh')
                                 print ('\033[36m╔═════════════════════════════════════════╗')
                                 print ('\033[37m║\033[37m [\033[32m+\033[37m] Url: '+url)
                                 print ('\033[37m║\033[37m [\033[32m+\033[37m] Url Berhasil di pendekan')
                                 print ("\033[37m║\033[37m [\033[32m√\033[37m] Hasil: " +putih +req.text)
                                 print ('\033[36m╚═════════════════════════════════════════╝')
                                 sys.exit()
                 except Exception as e:
                         print ("+[!] Error"+e)
                         sys.exit()

if __name__ == '__main__':
        os.system('clear')
        def angga():
                  print("Welcome Di Tools Shortlink")
                  print("Coded By SuryaPardana")
                  print("Selamat menggunakan")
                  angga()
        print ('\033[36m╔═════════════════════════════════════════╗')
        url = input('\033[37m║\033[37m [\033[32m*\033[37m] Url\033[31m: \033[37m')
        print ('\033[36m╚═════════════════════════════════════════╝')
        short().main(url)



