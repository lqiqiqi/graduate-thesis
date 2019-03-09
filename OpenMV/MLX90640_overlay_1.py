# MLX90640 Overlay Demo
#
# This example shows off how to overlay a heatmap onto your OpenMV Cam's
# live video output from the main camera.

import sensor, image, time, fir, builtins, gc, pyb, utime

rtc = pyb.RTC()
rtc.datetime((2019, 2, 28, 22, 17, 0, 0, 0))



#from pyb import Timer

#tim = Timer(3)
#tim.init(prescaler=1, period=1000000)

#def tick(timer):                # 还不知道怎么定时执行
    #print('timer')

#tim.callback(tick)


gc.enable()
gc.collect()

f = open('data.txt', 'w')
#f.write(str(utime.localtime()))
f.write('\n')
f.close()


ALT_OVERLAY = False # Set to True to allocate a second ir image.

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)

# Initialize the thermal sensor
fir.init(type=fir.FIR_MLX90640, refresh=12) # Hz (higher end OpenMV Cam's may be able to run faster)

# Allocate another frame buffer for smoother video.
extra_fb = sensor.alloc_extra_fb(sensor.width(), sensor.height(), sensor.RGB565)

# FPS clock
clock = time.clock()

while (True):
    clock.tick()

    # Capture an image
    img = sensor.snapshot()

    # Capture FIR data
    #   ta: Ambient temperature
    #   ir: Object temperatures (IR array)
    #   to_min: Minimum object temperature
    #   to_max: Maximum object temperature
    ta, ir, to_min, to_max = fir.read_ir()
    #aver = sum(ir)/len(ir)


    ir_img = []
    face = []
    for i in ir:
        if i - to_min > 7:
            ir_img.append(i)
            face.append(i)
        else:
            ir_img.append(to_min)
    if len(face) > 1:
        face_max = builtins.max(face)
        face_min = builtins.min(face)
        face_aver = sum(face) / len(face)
        print('mean:',face_aver, 'max:',face_max, 'min:', face_min)

    if not ALT_OVERLAY:
        # Scale the image and belnd it with the framebuffer
        #fir.draw_ir(img, ir)
        fir.draw_ir(img, ir_img)
    else:
        # Create a secondary image and then blend into the frame buffer.
        extra_fb.clear()
        fir.draw_ir(extra_fb, ir, alpha=256)
        img.blend(extra_fb, alpha=128)

    # Draw ambient, min and max temperatures.
    img.draw_string(8, 0, "Ta: %0.2f C" % ta, color = (255, 0, 0), mono_space = False)
    img.draw_string(8, 8, "To min: %0.2f C" % to_min, color = (255, 0, 0), mono_space = False)
    img.draw_string(8, 16, "To max: %0.2f C"% to_max, color = (255, 0, 0), mono_space = False)

    # Force high quality streaming...
    img.compress(quality=90)

    # Print FPS.
    #print(clock.fps())


    #str = builtins.input("请输入 过热0 热1 舒服2 冷3 过冷4：")
    #print ("你输入的内容是: ", str)



    f = open('data.txt', 'a')
    #time_ = utime.localtime()
    #f.write(str(time_))

    #f.write('\t')

    for i in ir:
        f.write(str(i))
        f.write('\t')

    f.write('\n')
    f.close()


    #pyb.delay(5000)

    del face, ir, ta, to_min, to_max, img, ir_img, i

    #print('mean:',aver, 'max:',to_max, 'min:', to_min)

