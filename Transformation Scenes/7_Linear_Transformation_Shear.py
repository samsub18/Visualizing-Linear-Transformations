from big_ol_pile_of_manim_imports import*

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

class ShearInXDirectionExplanation(Scene):
	def construct(self):
		t1 = TextMobject("This is a ","Shear"," in ","x ","direction")
		t1[1].set_color(YELLOW)
		t1[3].set_color(GREEN)
		self.play(Write(t1))
		self.wait()

class ShearInYDirectionExplanation(Scene):
	def construct(self):
		t1 = TextMobject("This is a ","Shear"," in ","y ","direction")
		t1[1].set_color(YELLOW)
		t1[3].set_color(RED)
		self.play(Write(t1))
		self.wait()


class ShearInXDirection(LinearTransformationScene):
	CONFIG = {
		"leave_ghost_vectors" : True,
	}
	def construct(self):
		matrix = [[1,1],[0,1]]
		object = Dot(color = DARK_BLUE)
		v = np.array([[2],[2]])
		self.add_vector(v)
		self.apply_matrix(matrix)
		self.wait()

class ShearInYDirection(LinearTransformationScene):
	CONFIG = {
		"leave_ghost_vectors" : True,
	}
	def construct(self):
		matrix = [[1,0],[1,1]]
		object = Dot(color = DARK_BLUE)
		v = np.array([[-1],[-1]])
		self.add_vector(v)
		self.apply_matrix(matrix)
		self.wait()