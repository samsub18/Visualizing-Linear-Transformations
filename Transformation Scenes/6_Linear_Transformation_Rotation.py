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

class AntiClockWiseRotation60Explanation(Scene):
	def construct(self):
		t1 = TextMobject("This is a 60 degree"," Anticlockwise Rotation")
		t1[1].set_color(YELLOW)
		self.play(Write(t1))
		self.wait()

class ClockWiseRotation30Explanation(Scene):
	def construct(self):
		t1 = TextMobject("This is a 30 degree"," Clockwise Rotation")
		t1[1].set_color(YELLOW)
		self.play(Write(t1))
		self.wait()

class AntiClockWiseRotation60(LinearTransformationScene):
	CONFIG = {
		"leave_ghost_vectors" : True,
		"angle" : np.pi/3,
	}
	def construct(self):
		matrix = [[np.cos(self.angle),-1*np.sin(self.angle)],[np.sin(self.angle),np.cos(self.angle)]]
		object = Dot(color = DARK_BLUE)
		self.add(object)
		v = np.array([[2],[1]])
		self.add_vector(v)
		self.apply_matrix(matrix)
		self.wait()


class ClockWiseRotation30(LinearTransformationScene):
	CONFIG = {
		"leave_ghost_vectors" : True,
		"angle" : np.pi/6,
	}
	def construct(self):
		matrix = [[np.cos(self.angle),np.sin(self.angle)],[-1*np.sin(self.angle),np.cos(self.angle)]]
		object = Dot(color = DARK_BLUE)
		self.add(object)
		v = np.array([[1],[1]])
		self.add_vector(v)
		self.apply_matrix(matrix)
		self.wait()