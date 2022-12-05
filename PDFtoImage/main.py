from pdf2image import convert_from_path
import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

pdf = sys.argv[1]
pages = convert_from_path(pdf, 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
