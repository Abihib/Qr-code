import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import (RoundedModuleDrawer )
from qrcode.image.styles.colormasks import (SolidFillColorMask)


for i in range(3):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data('https:///rassadka/' + str(i))
    qr = qr.make_image(image_factory=StyledPilImage,
                     color_mask=SolidFillColorMask((255,255,255),(0,47,112)),
                     module_drawer=RoundedModuleDrawer(),
                     #embeded_image_path="pngegg.png",
                     eye_drawer=RoundedModuleDrawer())
    qr.save('vmeste_' + str(i).rjust(0, '0') + '.png')





