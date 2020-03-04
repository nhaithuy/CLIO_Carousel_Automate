# a program to automatically generate carousel code for CLIO 
# @ThuyHNguyen2020

# class to create image objects
class CarouselItem(object):
  def __init__(self, url = "", alt = "", caption = "", w = 200, h = 200):
    self.url = url
    self.alt = alt
    self.caption = caption
    self.w = w
    self.h = h

# get the number of images. return an integer
def get_num_img():
  while (True):
    try:
      num_img = eval(input('Enter the number of images: '))
      return num_img
    except:
      pass
    
  return num_img

# get all the links, title, alts, captions, and sizes. return a list of images
def get_img_info(num_img):
  # initialize result list
  res = []

  for i in range(num_img):
    print('\nImage #' + str(i + 1) + '\n')
    url = input('Enter url: ')
    alt = input('Enter alt: ')
    caption = input('Enter caption: ')
    w = eval(input('Enter width: '))
    h = eval(input('Enter height: '))

    # create carousel item object
    carousel_item = CarouselItem(url, alt, caption, w, h)

    # store item in list
    res.append(carousel_item)
  
  return res

# generate an md-tab item for each image. return an html string
def make_md_tab(img_obj):
  res = '<md-tab flex="true" label="' + img_obj.caption + '" class="tabbed-content"><img src="' + img_obj.url + '" alt="' + img_obj.alt + '" width="' + str(img_obj.w) + '" height="' + str(img_obj.h) + '" /><br /><em><span style="color: #434652;">' + img_obj.caption + '</span></em></md-tab>'

  return res

# generate a wrapper md-tabs for all images
def make_md_tabs(img_lst):
  num_img = len(img_lst)

  # first add the start of the wrapper
  res = '<p style="text-align: center;"><md-tabs flex="true" md-dynamic-height="true" md-border-bottom="true"> '

  # loop over the img_lst
  for i in range(num_img):
    ind_md_tab = make_md_tab(img_lst[i])
    res += ind_md_tab

  # now add the closing 
  res += '</md-tabs></p>'

  return res

def main():
  # first get the number of images needed
  num_img = get_num_img()

  # prompt user to enter all images info
  img_data = get_img_info(num_img)

  # now generate the md_tabs string 
  res = make_md_tabs(img_data)

  # write the file
  out_file = open('result.txt', 'w+')
  out_file.write(res)

  # close the file 
  out_file.close()

  print('\nDone! Open result.txt to the left and copy your HTML code to CLIO')


main()