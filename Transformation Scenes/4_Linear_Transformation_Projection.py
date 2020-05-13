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

class ProjectionOnXAxisExplanation(Scene):
	def construct(self):
		t1 = TextMobject("Let's visualise a ","Projection on the X axis")
		t1[1].set_color(YELLOW)
		self.play(Write(t1))
		self.wait()

class ProjectionOnYAxisExplanation(Scene):
	def construct(self):
		t1 = TextMobject("Let's visualise a ","Projection on the Y axis")
		t1[1].set_color(YELLOW)
		self.play(Write(t1))
		self.wait()


class ProjectionOnXAxis(LinearTransformationScene):
	CONFIG = {
		"leave_ghost_vectors" : True,
	}
	def construct(self):
		v = np.array([[1],[2]])
		object = Dot(color = DARK_BLUE)
		self.add(object)
		matrix = [[1,0],[0,0]]
		self.add_vector(v)
		self.apply_matrix(matrix)
		self.wait()



class ProjectionOnYAxis(LinearTransformationScene):
	CONFIG = {
		"leave_ghost_vectors" : True,
	}
	def construct(self):
		v = np.array([[3],[-1]])
		object = Dot(color = DARK_BLUE)
		self.add(object)
		matrix = [[0,0],[0,1]]
		self.add_vector(v)
		self.apply_matrix(matrix)
		self.wait()
