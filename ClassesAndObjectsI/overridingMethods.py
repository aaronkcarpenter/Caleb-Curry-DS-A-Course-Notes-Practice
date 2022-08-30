def __str__(self):
    return f'Pan {str(self.pan)}. Tilt {str(self.tilt)}. Zoo{str(self.zoom)}'

def __eq__(self, other):
    return self.pan == other.pan and self.tilt == other.tilt and self.zoom == other.zoom
    
__hash__ == None