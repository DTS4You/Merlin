######################################################
### Main-Program                                   ###
### Projekt: Hera-Mission                          ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
import time                                                 # type: ignore


obj_offset = -1

pix_array_01 = [ 8]
pix_array_02 = [ 7]
pix_array_03 = [ 3]
pix_array_04 = [ 4]
pix_array_05 = [ 5]
pix_array_06 = [ 1, 2]
pix_array_07 = [ 9]
pix_array_08 = [ 6]
pix_array_09 = [10, 16]
pix_array_10 = [12, 18]
pix_array_11 = [15, 21]
pix_array_12 = [0]
pix_array_13 = [0]
pix_array_14 = [11, 17]
pix_array_15 = [13, 19]
pix_array_16 = [14, 20]


def blink_func():
    MyWS2812.do_blink()


# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    blink_couter = 0

    try:
        print("Start Main Loop")
 
        while MySerial.sercon_read_flag():

            if blink_couter > 50:
                blink_couter = 0
                #print("Blink Funktion")
                blink_func()
            
            MySerial.sercon_read_line()
            if MySerial.get_ready_flag():       # Zeichenkette empfangen
                #print(MySerial.get_string())
                MyDecode.decode_input(str(MySerial.get_string()))
                #MyDecode.decode_printout()
                if MyDecode.get_valid_flag() == True:
                    #print("Valid Command")
                    if MyDecode.get_cmd_1() == "do":
                        #print("do")
                        if MyDecode.get_cmd_2() == "all":
                            #print("all")
                            if MyDecode.get_value_1() == 0:
                                #print("off")
                                MyWS2812.do_all_off()
                            if MyDecode.get_value_1() == 1:
                                #print("on")
                                MyWS2812.do_all_on()
                            if MyDecode.get_value_1() == 2:
                                #print("def")
                                MyWS2812.do_all_def()
                        if MyDecode.get_cmd_2() == "obj":
                            #print("obj")
                            #print(MyDecode.get_value_1())
                            #print(segment_map[MyDecode.get_value_1()])
                            if MyDecode.get_value_1() == 1:
                                for i in pix_array_01:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 2:
                                for i in pix_array_02:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 3:
                                for i in pix_array_03:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 4:
                                for i in pix_array_04:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 5:
                                for i in pix_array_05:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 6:
                                for i in pix_array_06:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 7:
                                for i in pix_array_07:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 8:
                                for i in pix_array_08:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 9:
                                for i in pix_array_09:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 10:
                                for i in pix_array_10:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 11:
                                for i in pix_array_11:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 12:
                                for i in pix_array_12:
                                    # MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    pass
                            if MyDecode.get_value_1() == 13:
                                for i in pix_array_13:
                                    # MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    pass
                            if MyDecode.get_value_1() == 14:
                                for i in pix_array_14:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 15:
                                for i in pix_array_15:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                            if MyDecode.get_value_1() == 16:
                                for i in pix_array_16:
                                    MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())

                            #MyWS2812.set_led_obj(MyDecode.get_value_1(), MyDecode.get_value_2())

                            # ------------------------------------------------------------------
                            if MyDecode.get_value_1() == 81:
                                print("Motor 1 -> " + MyDecode.get_value_2())
                                if MyDecode.get_value_2() == "on":
                                    MyGPIO.i2c_write(0, True)
                                else:
                                    MyGPIO.i2c_write(0, False)
                            
                            if MyDecode.get_value_1() == 82:
                                print("Motor 1 -> " + MyDecode.get_value_2())
                                if MyDecode.get_value_2() == "on":
                                    MyGPIO.i2c_write(1, True)
                                else:
                                    MyGPIO.i2c_write(1, False)

                            if MyDecode.get_value_1() == 83:
                                print("Motor 1 -> " + MyDecode.get_value_2())
                                if MyDecode.get_value_2() == "on":
                                    MyGPIO.i2c_write(2, True)
                                else:
                                    MyGPIO.i2c_write(2, False)
                                
                            if MyDecode.get_value_1() == 84:
                                print("Motor 1 -> " + MyDecode.get_value_2())
                                if MyDecode.get_value_2() == "on":
                                    MyGPIO.i2c_write(3, True)
                                else:
                                    MyGPIO.i2c_write(3, False)

                            if MyDecode.get_value_1() == 85:
                                print("Motor 1 -> " + MyDecode.get_value_2())
                                if MyDecode.get_value_2() == "on":
                                    MyGPIO.i2c_write(4, True)
                                else:
                                    MyGPIO.i2c_write(4, False)

                            if MyDecode.get_value_1() == 86:
                                print("Motor 1 -> " + MyDecode.get_value_2())
                                if MyDecode.get_value_2() == "on":
                                    MyGPIO.i2c_write(5, True)
                                else:
                                    MyGPIO.i2c_write(5, False)

                    if MyDecode.get_cmd_1() == "test":
                        #print("Test")
                        if MyDecode.get_cmd_2() == "led":
                            #print("LED")
                            MyWS2812.test_led(MyDecode.get_value_1(), MyDecode.get_value_2())
                    

            blink_couter = blink_couter + 1
            # Loop-Delay !!!
            time.sleep(0.01)        # 10ms
    
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")   

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_i2c:
        #print("I2C_MCP23017 -> Load-Module")
        import libs.module_i2c as MyGPIO
        #print("I2C -> Setup")
        MyGPIO.i2c_setup()
        ### Test ###
        print("I2C -> SetOutput")
        MyGPIO.i2c_write(0,True)
        time.sleep(0.5)
        MyGPIO.i2c_write(0,False)

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import libs.module_ws2812_v3 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        #print("WS2812 -> Run self test")
        MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        #print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
