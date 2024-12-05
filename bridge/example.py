from abc import ABC, abstractmethod

class IRenderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float):
        pass

    @abstractmethod
    def render_rectangle(self, width: float, height: float):
        pass

class Shape(ABC):
    def __init__(self, renderer: IRenderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass


class OpenGLRenderer(IRenderer):
    def render_circle(self, radius: float):
        print(f"Rendering a circle with radius {radius} using OpenGL")

    def render_rectangle(self, width: float, height: float):
        print(f"Rendering a rectangle with width {width} and height {height} using OpenGL")

class DirectXRenderer(IRenderer):
    def render_circle(self, radius: float):
        print(f"Rendering a circle with radius {radius} using DirectX")

    def render_rectangle(self, width: float, height: float):
        print(f"Rendering a rectangle with width {width} and height {height} using DirectX")


class Circle(Shape):
    def __init__(self, renderer: IRenderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

class Rectangle(Shape):
    def __init__(self, renderer: IRenderer, width: float, height: float):
        super().__init__(renderer)
        self.width = width
        self.height = height

    def draw(self):
        self.renderer.render_rectangle(self.width, self.height)


if __name__ == "__main__":
    # Use OpenGL Renderer
    opengl_renderer = OpenGLRenderer()
    circle = Circle(opengl_renderer, 5)
    rectangle = Rectangle(opengl_renderer, 10, 6)

    circle.draw()
    rectangle.draw()

    # Switch to DirectX Renderer
    directx_renderer = DirectXRenderer()
    circle = Circle(directx_renderer, 7)
    rectangle = Rectangle(directx_renderer, 15, 8)

    circle.draw()
    rectangle.draw()
