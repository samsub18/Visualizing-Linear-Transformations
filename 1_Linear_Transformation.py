from big_ol_pile_of_manim_imports import *

def quadratic(point):
    x, y, z = point
    return (y**2)*UP + RIGHT

class Introduction(Scene):
	def construct(self):
		t1 = TexMobject(r"Visualzing\quad Linear\quad Transformations")
		t2 = TexMobject(r"Using\quad python\quad \& \quad manim")
		t3 = TexMobject(r"Sameer\quad Prasad\quad Subhedar")
		t4 = TexMobject("PES2201800323")
		self.play(Write(t1))
		self.play(Transform(t1,t2))
		self.wait()
		self.play(Transform(t1,t3))
		self.wait()
		self.play(Transform(t1,t4))
		self.wait()

class Introduction_2(Scene):
	def construct(self):
		t1 = TextMobject("This is how a","Linear Transformation", "looks like")
		t1[1].set_color(YELLOW)
		self.play(Write(t1))
		self.wait()	

class LinearTransformationExample(LinearTransformationScene):
    CONFIG = {
        "leave_ghost_vectors": True,
    }
    def construct(self):
        matrix = [[1, 1], [0, 1]] #Shear
        object = Dot(color = YELLOW)
        self.add(object)
        self.apply_matrix(matrix)
        self.wait()

class Introduction_3(Scene):
	def construct(self):
		t1 = TextMobject("This is how a","Nonlinear Transformation", "looks like")
		t1[1].set_color(YELLOW)
		self.play(Write(t1))
		self.wait()	


class NonlinearTransformationExample(LinearTransformationScene):
    CONFIG = {
        "leave_ghost_vectors": True,
        "angle" : np.pi/3,
    }

    def construct(self):
        self.setup()
        object = Dot(color = YELLOW)
        self.add(object)
        self.wait()
        self.apply_nonlinear_transformation(self.func)
        self.wait()

    def func(self, point):
        return quadratic(point)