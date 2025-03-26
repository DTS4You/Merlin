# #############################################################################
# ### MyGlobal
# ### Merlin V1.00
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = False
    inc_serial          = False
    inc_i2c             = False


class Global_WS2812:

    numpix_1            = 16            # Anz. LEDs im 1. Stripe -> Boden 1
    numpix_2            = 16            # Anz. LEDs im 2. Stripe -> Boden 2
    numpix_3            = 16            # Anz. LEDs im 3. Stripe -> Boden 3
    numpix_4            = 16            # Anz. LEDs im 4. Stripe -> Boden 4
    numpix_5            = 16            # Anz. LEDs im 5. Stripe -> Boden 5
    numpix_6            = 256           # Anz. LEDs im 6. Stripe -> Spiegel, Laser, Empfänger
    #numpix_1           = 256           # Anz. LEDs im 1. Stripe -> Test !!!

    #seg_01_strip        = 0             #  1. Seg -> Stripe      # 0 -> Spiegel -> Ring
    #seg_01_start        = 0             #  1. Seg -> Start
    #seg_01_count        = 68            #  1. Seg -> Anzahl

    #seg_02_strip        = 0             #  2. Seg -> Stripe      # 1 -> Laser Sender
    #seg_02_start        = 68            #  2. Seg -> Start
    #seg_02_count        = 23            #  2. Seg -> Anzahl

    #seg_03_strip        = 0             #  3. Seg -> Stripe      # 2 -> Laser Empfänger
    #seg_03_start        = 91            #  3. Seg -> Start
    #seg_03_count        = 16            #  3. Seg -> Anzahl
    
    #--------------------------------------------------------------------------

    seg_01_strip        = 0             #  1. Seg -> Stripe      # 0 -> Boden 1
    seg_01_start        = 0             #  1. Seg -> Start
    seg_01_count        = 16            #  1. Seg -> Anzahl

    seg_02_strip        = 1             #  2. Seg -> Stripe      # 1 -> Boden 2
    seg_02_start        = 0             #  2. Seg -> Start
    seg_02_count        = 16            #  2. Seg -> Anzahl

    seg_03_strip        = 2             #  3. Seg -> Stripe      # 2 -> Boden 3
    seg_03_start        = 0             #  3. Seg -> Start
    seg_03_count        = 16            #  3. Seg -> Anzahl

    seg_04_strip        = 3             #  4. Seg -> Stripe      # 3 -> Boden 4
    seg_04_start        = 0             #  4. Seg -> Start
    seg_04_count        = 16            #  4. Seg -> Anzahl

    seg_05_strip        = 4             #  5. Seg -> Stripe      # 4 -> Boden 5
    seg_05_start        = 0             #  5. Seg -> Start
    seg_05_count        = 16            #  5. Seg -> Anzahl
    
    seg_06_strip        = 5             #  6. Seg -> Stripe      # 5 -> Spiegel
    seg_06_start        = 0             #  6. Seg -> Start
    seg_06_count        = 200           #  6. Seg -> Anzahl
    
    seg_07_strip        = 6             #  7. Seg -> Stripe      # 5 -> Laser
    seg_07_start        = 200           #  7. Seg -> Start
    seg_07_count        = 16            #  7. Seg -> Anzahl

    seg_08_strip        = 7             #  8. Seg -> Stripe      # 5 -> Empfänger
    seg_08_start        = 216           #  8. Seg -> Start
    seg_08_count        = 16            #  8. Seg -> Anzahl
    
# -----------------------------------------------------------------------------

    color_def           = (  0,  0,  2)
    color_off           = (  0,  0,  0)
    color_on            = (255, 20, 20)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (255, 20, 20)
    color_blink_off     = (  0,  0,  5)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
