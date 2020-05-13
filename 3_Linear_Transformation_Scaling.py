from big_ol_pile_of_manim_imports import *


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

class ExplaningGrowth(Scene):
	def construct(self):
		t1 = TextMobject("This is how a vector","grows","when multiplied by a number","greater than 1")
		t1[1].set_color(GREEN)
		t1[3].set_color(BLUE)
		t1[0].move_to(1.5*UP)
		t1[1].move_to(1*UP)
		t1[2].move_to(0.5*UP)
		t1[3].move_to(0)
		self.play(Write(t1))
		self.wait(1.5)

class ExplaningShrink(Scene):
	def construct(self):
		t1 = TextMobject("This is how a vector","shrinks","when multiplied by a number","greater than 0 but","less than 1")
		t1[1].set_color(RED)
		t1[3].set_color(BLUE)
		t1[4].set_color(BLUE)
		t1[0].move_to(1.5*UP)
		t1[1].move_to(1*UP)
		t1[2].move_to(0.5*UP)
		t1[3].move_to(0)
		t1[4].move_to(0.5*DOWN)
		self.play(Write(t1))
		self.wait(1.5)

class ExplaningChangeShrinkGrow(Scene):
	def construct(self):
		t1 = TextMobject("This is how a vector","changes direction","\& then","grows or shrinks when","multiplied by a negative number")
		t1[1].set_color(YELLOW)
		t1[3].set_color(GREEN)
		t1[0].move_to(1.5*UP)
		t1[1].move_to(1*UP)
		t1[2].move_to(0.5*UP)
		t1[3].move_to(0*DOWN)
		t1[4].move_to(0.5*DOWN)
		self.play(Write(t1))
		self.wait(1.5)


class ScalingGrow(LinearTransformationScene):
    CONFIG = {
        "leave_ghost_vectors": True,
    }
    def construct(self):
    	v = np.array([[1],[1]])
    	object = Dot(color = DARK_BLUE)
    	matrix = [[2,0],[0,2]]
    	self.add(object)
    	self.add_vector(v)
    	self.apply_matrix(matrix)
    	self.wait()

class ScalingShrink(LinearTransformationScene):
    CONFIG = {
        "leave_ghost_vectors": True,
    }
    def construct(self):
    	v = np.array([[1],[1]])
    	object = Dot(color = DARK_BLUE)
    	self.add(object)
    	matrix = [[1/3,0],[0,1/3]]
    	self.add_vector(v)
    	self.apply_matrix(matrix)
    	self.wait()

class ScalingChangingDirectionGrowShrink(LinearTransformationScene):
    CONFIG = {
        "leave_ghost_vectors": True,
    }
    def construct(self):
    	v = np.array([[1],[1]])
    	object = Dot(color = DARK_BLUE)
    	self.add(object)
    	matrix_1 = [[-1,0],[0,-1]]
    	matrix_2 = [[2,0],[0,2]]
    	matrix_3 = [[1/3,0],[0,1/3]]
    	self.add_vector(v)
    	self.apply_matrix(matrix_1)
    	self.wait()
    	self.apply_matrix(matrix_2)
    	self.wait()
    	self.apply_matrix(matrix_3)
    	self.wait()