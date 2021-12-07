# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [ 
                [0, 0, 0 ], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],      
                [0, self.parameters['thickness'], 0],
                [0, self.parameters['thickness'],  self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], 0],
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
                ]

        self.faces = [
                # définir ici les faces
                [0, 3, 2, 1],
                [0, 3, 6, 4],
                [2, 3, 6, 7],
                [6, 7, 5, 4],
                [1, 2, 7, 5],
                [1, 0, 4, 5]
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
    
        test=True
        if (self.parameters['height']>=x.getParameter('height')+x.getParameter('position')[2]-self.parameters['position'][2])==False:
            test=False
        if (x.getParameter('position')[2]>=self.parameters['position'][2])==False:
            test=False
        if (self.parameters['width']>=x.getParameter('width')+x.getParameter('position')[0]-self.parameters['position'][0])==False:
            test=False
        if (x.getParameter('position')[0]>=self.parameters['position'][0])==False:
            test=False
    
        return test   
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        self.object            
        
    # Draws the edges
    def drawEdges(self):
        for i in range (0,len(self.faces)):
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)
            gl.glPushMatrix()
            gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
            gl.glColor3fv([0.8, 0.8, 0.8]) # Couleur gris moyen
            gl.glVertex3fv(self.vertices[self.faces[i][0]])
            gl.glVertex3fv(self.vertices[self.faces[i][1]])
            gl.glVertex3fv(self.vertices[self.faces[i][2]])
            gl.glVertex3fv(self.vertices[self.faces[i][3]])
            gl.glEnd()
            gl.glPopMatrix()            
    # Draws the faces
    def draw(self):
        if self.parameters['edges']==True:
            self.drawEdges()
        # A compléter en remplaçant pass par votre code
        for i in range (0,len(self.faces)):
          gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_FILL) # on trace les faces : GL_FILL
          gl.glPushMatrix()
          gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
          gl.glColor3fv([0.2, 0.2, 0.2]) # Couleur gris moyen
          gl.glVertex3fv(self.vertices[self.faces[i][0]])
          gl.glVertex3fv(self.vertices[self.faces[i][1]])
          gl.glVertex3fv(self.vertices[self.faces[i][2]])
          gl.glVertex3fv(self.vertices[self.faces[i][3]])
          gl.glEnd()
          gl.glPopMatrix()