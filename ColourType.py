class Colour:
    """
        A data type, that saves colour data. 
        It has rgb, rgba, alpha, and hex values stored within it.
    """
    def __init__(self):
        """"""
        #rgb
        self._rgb = [0,0,0]
        self._alpha = 1.0
        self._rgba = self._rgb + [self._alpha]
        #hex
        self._hex = "#FFFFFF"
    
    @property
    def rgb(self):
        """
        Red, Green, Blue.
        Is a way of representing the value of how much,
        of the three colour's light their is.
        Stored as a list with length three as [r, g, b].
        The 'r', 'g', and 'b' values need to be integers between 255 and 0, inclusive.
        """
        return self._rgb
    
    @rgb.setter    
    def rgb(self, arr: list):
        #check list
        if type(arr) != list:
            raise TypeError ("The Rgb value needs to be a list")
        if len(arr) != 3:
            raise IndexError ("The Rgb value needs a length of 3")
        
        r = arr[0]
        g = arr[1]
        b = arr[2]
        
        #check values are correct type (integer)
        if type(r) != int:
            raise TypeError ("The Red value needs to be an integer, not a", type(r))
        if type(g) != int:
            raise TypeError ("The Green value needs to be an integer, not a", type(g))
        if type(b) != int:
            raise TypeError ("The Blue value needs to be an integer, not a", type(b))
        
        #check the numbers are in the correct range
        if  (255 >= r >= 0) == False:
            raise IndexError ("The Red value needs to be between 0 and 255 inclusive")
        if  (255 >= g >= 0) == False:
            raise IndexError ("The Green value needs to be between 0 and 255 inclusive")
        if  (255 >= b >= 0) == False:
            raise IndexError ("The Blue value needs to be between 0 and 255 inclusive")

        #set values
        self._rgb = [r,g,b]
        self._hex = self.toHex(self._rgb)
        self._rgba = [self._rgb]  + [self._alpha]
    
    @property
    def rgba(self):
        """
        Red, Green, Blue, Alpha
        Is like rgb, but offers more information as it contains the alpha value.
        Is stored as a list of length 4, [r, g, b, a].
        The 'r', 'g', and 'b' values need to be integers between 255 and 0, inclusive.
        The 'a' value needs to be an integer or float between 1 and 0, inclusive.
        """
        return self._rgba
    
    @rgba.setter
    def rgba(self, arr: list):
        #check list
        if type(arr) != list:
            raise TypeError ("The Rgba value needs to be a list")
        if len(arr) != 4:
            raise IndexError ("The Rgba value needs a length of 3")
        
        r = arr[0]
        g = arr[1]
        b = arr[2]
        a = arr[3]
        
        #check values are correct type (integer)
        if type(r) != int:
            raise TypeError ("The Red value needs to be an integer, not a", type(r))
        if type(g) != int:
            raise TypeError ("The Green value needs to be an integer, not a", type(g))
        if type(b) != int:
            raise TypeError ("The Blue value needs to be an integer, not a", type(b))
        if (type(a) != int) and (type(a) != float):
            raise TypeError ("The Alpha value needs to be an integer or a float, not a", type(a))
        
        #check the numbers are in the correct range
        if  (255 >= r >= 0) == False:
            raise IndexError ("The Red value needs to be between 0 and 255, inclusive")
        if  (255 >= g >= 0) == False:
            raise IndexError ("The Green value needs to be between 0 and 255, inclusive")
        if  (255 >= b >= 0) == False:
            raise IndexError ("The Blue value needs to be between 0 and 255, inclusive")
        if  (1 >= a >= 0) == False:
            raise IndexError ("The Alpha value needs to be between 0 and 1, inclusive")
        

        #set values
        self._rgba = [r, g, b, a]
        self._rgb = [r,g,b]
        self._hex = Colour.toHex(self._rgb)
        
    @property
    def alpha(self):
        """
        The opacity variable.
        Needs to be set between 0 and 1, inclusive.
        Needs to be an integer or float.
        """
        return self._alpha
    
    @alpha.setter
    def alpha(self, value):
        #error check
        if (type(value) != int) and (type(value) != float):
            raise TypeError ("The Alpha value needs to be an integer or a float, not a", type(value))
        if  (1 >= value >= 0) == False:
            raise IndexError ("The Alpha value needs to be between 0 and 1, inclusive")
        
        self._alpha = value
        self._rgba = self._rgb + [value]
    
    @property
    def hex(self):
        """
        Is a method of storing colour data
        Starts with a hashtag '#', and is then followed by six hexadecimal digits.
        These digits can be broken down into three sections of two digits.
        each section of hexadecimal numbers represent a corresponding rgb value.
        So the first two numbers is the red value of rgb, but in hexadecimal.
        The third and fourth are the blue value numbers, 
        and the fith and sixth are the green value numbers.
        The Hexadecimal sections can range from '00' up to 'FF'.
        If setting manualy remeber to have the hashtag infront of the number.
        Saved as a string of length seven, including the hashtag.
        """
        return self._hex
    
    @hex.setter
    def hex(self, arr : str):
        #error check
        if type(hex) != str:
            raise TypeError ("The Hex value needs to be a string, not a", type(hex))
        if len(hex) != 7:
            raise IndexError ("The Hex code shoudl only be 7 characters, including the hashtag")
        
        #set values
        self._hex = arr
        self._rgb = self.toRgb(arr)
        self._rgba = self._rgb + [self._alpha]


    #converters
    @classmethod
    def toHex(cls, rgb: list):
        """
        Converts a given rgb value into a hex value. 
        The given rgb value needs to be in a list format.
        The returned Hex value is a string, with a hashtag at the front.
        """
        #error check
        if type(rgb) != list:
            raise TypeError ("The Rgb value needs to be a list, not a", type(rgb))
        if len(rgb) != 3:
            raise IndexError ("The Rgb value needs a length of 3")
        
        #convert
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2]).upper()
    
    @classmethod
    def toRgb(self, hex: str):
        """
        Converts a given hex value into an rgb value. 
        The given hex value needs to be a string, with a hashtag infront.
        The returned rgb value is a list.
        """
        #error check
        if type(hex) != str:
            raise TypeError ("The Hex value needs to be a string, not a", type(hex))
        if len(hex) != 7:
            raise IndexError ("The Hex code shoudl only be 7 characters including the hashtag")
        
        #convert
        r = int(hex[1:3],16)
        g = int(hex[3:5],16)
        b = int(hex[5:7],16)
        return [r, g, b]
    
if __name__ == "__main__":
    col = Colour()
    col.rgb = [255,0,254]
    print(f"the rgb colour: {col.rgb}")
    print(f"Is the same as the hex ccolour: {col.hex}")