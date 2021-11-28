# by billythegoat356//
#RM by LixoInGitHub7564
# https://github.com/billythegoat356/Pandore
#  github.com/LixoInGitHub7564/Sega


from os import name, chdir
from os.path import isfile
from PIL import Image
from pystyle import Anime, Colorate, Colors, Center, System, Write




class build:
  def __init__(self, imagepath: str, scale: int) -> None:
    self.path = imagepath
    self.scale = scale

    return self.run()

  def run(self) -> None:
    img = self.mkimage(path=self.path)
    pixels = self.mkpixels(img=img)
    ascii = self.mkascii(pixels=pixels)

    with open(self.npath, mode="w", encoding='utf-8') as f:
      f.write(ascii)
    
    return None

  def mkimage(self, path: str) -> object:
    img = Image.open(path)
    width, height = img.size

    self.nwidth = round(width / self.scale)

    img = img.resize((self.nwidth, round(height / (self.scale * 2))))

    return img.convert('L')

  def mkpixels(self, img: object) -> str:
    pixels = img.getdata()

    pixels = [self.chars[pixel//25] for pixel in pixels]
    return ''.join(pixels).replace('.',' ')

  def mkascii(self, pixels: str) -> str:
    ascii = [pixels[index:index + self.nwidth] for index in range(0, len(pixels), self.nwidth)]
    nascii = []
    for line in ascii:
      if line.strip():
        nascii.append(line)
    return "\n".join(nascii)

  @property
  def npath(self) -> str:
    return ".".join(self.path.split(".")[:-1]) + ".txt"

  @property
  def chars(self) -> str:
    return ["§","/","#","&","@","$","%","*","!",":","."]



ascii = """
    !%$$$$%!     :*%%%%%%%:     :*$$$$%!       :%%%%%%*
  :@////////@:   :#/////§/!    $////////@:     %///////:
  !////S$////!   :#/E//$$$:   !//G/@%////$     @///A///*
  !////&$$%%%:   :#///#!::    %////$!####$    :#///&///@
   $#////#@*     :#////#/&    %////@%%%%%*    *///#$///#:   
   :%&/////&:   :#////##&    %////&/////@    $///&*////!             
 !&&&&$$////$    #///#:      %////@*////@    &///#&////$          
 :////$!////$    #////$%%   !*////@*////@   :#////#////&              
  $////////#!:   #//////§   %:@/////////@   *////&:#////!        
   !%@@@@$*:    :%$$$$$$$   !  *$@@@*%$$*   *$$$$* %$$$$!    
"""[1:]


flower = '''
              %*:                  ::                               
  !##@%*!!*%$$@@@@$%*:  *@$*:   !                       
   :@////§§§§/////§§§§#$!:%//@*:!@!                     
     !$&##//#///§§/&&#§§§#*$§§§/@%#@:                   
         ::!*$&#&#§§&$$&§/@&#&#/§§/§§$!$                
       !*%$/§§§§§##§/&&%%%§§§§§§///####§%               
      :!!!&§/#@$&##//§§§@@/§§§§§§§§§§/&@&%              
        */§/§§§#&###/§§§§§//§§§§/////§§§#/&&!        :  
       %§/#§§§§§§/§§§///§§§§§§§§##/&!%&//§§§#:      *@  
     !#§§&/######/§§§§§§§§§§§§§§#@§/#&&&//§§§#*:*  *§%  
   !% %§&/§§§§§/§§§§§§§§§§§§§/#&#&/§/#//§§§§/##§//§§$   
    %@$§#&#&@@&#///////§§§§§§§§/&§§§/##§§§/#/§§§#:$§/:  
   !% %§&/§§§§§/§§§§§§§§§§§§§/#&#&/§/#//§§§§/##§//§§$   
   !% %§&/§§§§§/§§§§§§§§§§§§§/#&#&/§/#//§§§§/##§//§§$   
   !% %§&/§§§§§/§§§§§§§§§§§§§/#&#&/§/#//§§§§/##§//§§$   
      %§##§§§§§#§§§////§§§§§§////&@$@##///§§§§#*#§&/:   
     :#§§@§§§§&$@&&#/§§§§/#&!*%@#§§§$!!**&@$§#§&&§§/:   
     $@&§&&§/&&##/§§#§/&#/§§$    :%#§§$*:: !!!@&/#§#    
    :@:!§§@#§§§§§&§§@&#§§§§§§&:     %/§§@@!!:: !*&#*    
    ::  %§§@#§§§§/@%@////////§&!     !/§§§/§&#$! :!     
         @§§@&§§§§/@$&##//§§§§§§&*   :%&###@$*:         
         */#§&@§§§§§/&#§§§§§§§§§§§#%:                   
         :&:&§&$§§§§§§#@&§§§§§§§§§§§$                   
          %::/§$@§§§§§§§#$&///####§§§@                  
             @§/*§§§§§§§§§%*##/§§§§§§§@                 
            !/§#*§§§§§§§§§§%&§§§§§§§§§§*                
            :!$!$§§§§§§§§§§/!§§§§§§/&$!:                
                :!%$@&&&##&&:%$%*!:
                '''[1:]




System.Size(140, 40)
System.Title("Sega By Lixo-")
System.Clear()
Anime.Fade(Center.Center(flower), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)



def main():
  System.Clear()
  print("\n"*2)
  print(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(ascii)))
  print("\n"*5)
  
  file = Write.Input("Drag an image -> ", Colors.green_to_yellow, interval=0.005)
  
  if not isfile(file):
      print()
      print(Colorate.Error("Error! This file does not exist!"))
      return

  scale = Write.Input("Enter the scale (recommended: 8) -> ", Colors.green_to_yellow, interval=0.005)
  
  try:
    scale = int(scale)
  except:
    print()
    print(Colorate.Error("Error! The scale has to be an integer"))
    return

  build(imagepath=file, scale=scale)
  
  print()
  Write.Input("Done!", Colors.green_to_yellow, interval=0.005)
  return exit()
        

if __name__ == '__main__':
    while True:
        main()
