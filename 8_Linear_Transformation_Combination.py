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

class ReflectionThenShearExplanation(Scene):
	def construct(self):
		t1 = TextMobject("Example of ","Reflection ","followed by"," Shear")
		t1[1].set_color(YELLOW)
		t1[3].set_color(RED)
		self.play(Write(t1))
		self.wait()

class RotationThenProjectionOnXAxisExplanation(Scene):
	def construct(self):
		t1 = TextMobject("Example of ","Rotation ","followed by"," Projection")
		t1[1].set_color(YELLOW)
		t1[3].set_color(RED)
		self.play(Write(t1))
		self.wait()

class ReflectionThenShear(LinearTransformationScene):
	CONFIG = {
		"leave_ghost_vectors":True,
	}
	def construct(self):
		mat_1 = [[-1,0],[0,-1]]
		object = Dot(color = DARK_BLUE)
		self.add(object)
		mat_2 = [[1,1],[0,1]]
		v = np.array([[-1],[2]])
		self.add_vector(v)
		self.apply_matrix(mat_1)
		self.apply_matrix(mat_2)
		self.wait()

class RotationThenProjectionOnXAxis(LinearTransformationScene):
	CONFIG = {
		"leave_ghost_vectors" : True,
		"angle" : 2*(np.pi/3)
	}
	def construct(self):
		mat_1 = [[np.cos(self.angle),-1*np.sin(self.angle)],[np.sin(self.angle),np.cos(self.angle)]]
		mat_2 = [[1,0],[0,0]]
		object = Dot(color = DARK_BLUE)
		self.add(object)
		v = np.array([[2],[1]])
		self.add_vector(v)
		self.apply_matrix(mat_1)
		self.apply_matrix(mat_2)
		self.wait()

