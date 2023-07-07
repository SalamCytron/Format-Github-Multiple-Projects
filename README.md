# Cytron Product Name/Tutorial Name
If you are new to [Cytron Product Name] and want to get started quickly, you are in the right place! Here you will find all the information you need to set up your hardware and software and start coding with the [Cytron Product Name].  


![Image of Cytron Product](https://github.com/SalamCytron/Format-Github-Multiple-Platforms/blob/main/cytron_product_image.png)


## Requirements  
To get started, you will need the following hardware and software:  
**Hardware:**  
* [Maker Pi Pico](https://www.cytron.io/p-maker-pi-pico) or [Maker Pi Pico Base](https://www.cytron.io/p-maker-pi-pico-nb)  
* [Raspberry Pi Pico](https://www.raspberrypi.org/documentation/pico/getting-started/)  
* [OLED Display SSD1306](https://my.cytron.io/p-oled-i2c-0.96inch-128x64-blue-display)  
* [3V3 I2C and SPI 1602 Serial Character LCD](https://my.cytron.io/p-3v3-i2c-and-spi-1602-serial-character-lcd)  


**Software:**  
To upload the code to the Raspberry Pi Pico you need an IDE such as [Micropython](https://micropython.org/download/).
These codes were written in python, if your operating system don't have it you can download it from [here](https://www.python.org/downloads/).

## Installation 
Inside the python file display_oled.py, edit the pin if you are using different port:

```python
i2c = io.I2C(board.GP1, board.GP0)
```
## Tutorials  
If you want a guidance on how to use the code for [Cytron Product Name], here some tutorials you can follow:
* [Real-Time Multitasking on Maker Pi Pico Using pyRTOS](https://cytron.io/tutorial/real-time-multitasking-on-maker-pi-pico-using-pyrtos)  
* [Building Line Following Robot Using Maker Pi Pico, Maker Drive and Maker Line](https://cytron.io/tutorial/building-line-following-robot-using-maker-pi-pico-maker-drive-and-maker-line)  
* [Play MP3 File on Maker Pi Pico Using Circuitpython](https://cytron.io/tutorial/play-mp3-file-on-maker-pi-pico-using-circuitpython)  
* [Read and Display Environment Sensor Data Using Raspberry Pi Pico and Circuitpython](https://cytron.io/tutorial/read-and-display-environment-sensor-data-using-raspberry-pi-pico-and-circuitpython)  


## Documentation  
For more information on the [Cytron Product Name], check out the datasheet here:
* [Cytron Product Datasheet](https://docs.google.com/document/d/1JoHsZk5IipQPCLXWbZYpDKjGlnkyACOJ1taUrKVsRg8/edit)  

## Support
If you need further assistance, we welcome you to our [technical forum](http://forum.cytron.io) or you can contact us through email support@cytron.io where our team will be happy to assist you. 

Let's start building with [Cytron Product Name]!

