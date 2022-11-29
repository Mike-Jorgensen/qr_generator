import qrcode
import inquirer
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *


#website_link = input('Input a URL: ')




def style_selection():

    drawer = [
    inquirer.List('style',
                    message="What style do you want?",
                    choices=['Square Module Drawer', 
                        'Gapped Square Module Drawer',
                        'Circle Module Drawer', 
                        'Rounded Module Drawer',
                        'Vertical Bars Drawer',
                        'Horizontal Bars Drawer'],
                ),
    ]
    qr_drawer = inquirer.prompt(drawer)

    if any([True for k,v in qr_drawer.items() if v == 'Square Module Drawer']):
        return SquareModuleDrawer()
    elif any([True for k,v in qr_drawer.items() if v == 'Horizontal Bars Drawer']):
        return HorizontalBarsDrawer()
    elif any([True for k,v in qr_drawer.items() if v == 'Gapped Square Module Drawer']):
        return GappedSquareModuleDrawer()
    elif any([True for k,v in qr_drawer.items() if v == 'Circle Module Drawer']):
        return CircleModuleDrawer()
    elif any([True for k,v in qr_drawer.items() if v == 'Rounded Module Drawer']):
        return RoundedModuleDrawer()
    elif any([True for k,v in qr_drawer.items() if v == 'Vertical Bars Module Drawer']):
        return VerticalBarsDrawer()
    else:
        pass

def color_mask_selection():
    mask = [
    inquirer.List('style',
                    message="What style do you want?",
                    choices=['Solid Fill Color Mask', 
                        'Radial Gradiant Color Mask',
                        'Square Gradiant Color Mask', 
                        'Horizontal Gradiant Color Mask',
                        'Vertical Gradiant Color Mask',
                        'Image Color Mask'],
                ),
    ]
    qr_mask = inquirer.prompt(mask)

    if any([True for k,v in qr_mask.items() if v == 'Solid Fill Color Mask']):
        return SolidFillColorMask()
    elif any([True for k,v in qr_mask.items() if v == 'Radial Gradiant Color Mask']):
        return RadialGradiantColorMask()
    elif any([True for k,v in qr_mask.items() if v == 'Square Gradiant Color Mask']):
        return SquareGradiantColorMask()
    elif any([True for k,v in qr_mask.items() if v == 'Horizontal Gradiant Color Mask']):
        return HorizontalGradiantColorMask()
    elif any([True for k,v in qr_mask.items() if v == 'Vertical Gradiant Color Mask']):
        return VerticalGradiantColorMask()
    elif any([True for k,v in qr_mask.items() if v == 'Image Color Mask']):
        return ImageColorMask()
    else:
        pass


qr = qrcode.QRCode(version = None, 
                #box_size = box_size_input, 
                #border = border_input,
                error_correction = qrcode.constants.ERROR_CORRECT_L,
                image_factory=StyledPilImage,
                )

qr.add_data('https://google.com')
qr.make(fit=True)


img = qr.make_image(back_color = "black",
                fill_color = "white",
                module_drawer=style_selection(),
                color_mask=color_mask_selection()
                )

img.save('my_qr.png')



# TODO:
# Allow users to customize the QR code generated.
# Automate the process to create multiple QR codes.
# Include more functions (or object parameters) of the qrcode library.
# Try changing the colors and styles of the generated QR codes using different drawer modules and fill colors.
# Use an application library (like Tkinter) to add a user interface.
# Check out other QR code libraries like pyqrcode.