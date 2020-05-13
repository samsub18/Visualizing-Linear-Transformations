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


class Matrix2D(Scene):
	def construct(self):
		t1 = TextMobject("This is a","2D","matrix")
		t1[1].set_color(RED)
		# grid = ScreenGrid()
		mat = TexMobject(r"\begin{bmatrix} -1 & \quad 1 \\ 1 & -1 \end{bmatrix}")
		mat.set_color(RED)
		t2 = TextMobject("This is an", "input", "vector")
		t2[1].set_color(YELLOW)
		t3 = TextMobject("This results in")
		t3.set_color(BLUE)
		mat2=TexMobject(r"\begin{bmatrix} 1 \\ 2 \end{bmatrix}")
		mat2.set_color(YELLOW)
		mat3 = TexMobject(r"=\quad 1\begin{bmatrix} -1 \\ 1 \end{bmatrix}\quad +\quad 2\begin{bmatrix} \quad 1 \\ -1 \end{bmatrix}")
		mat3.set_color(BLUE)
		mat4 = TexMobject(r"=\quad \begin{bmatrix} \quad 1 \\ -1 \end{bmatrix}")
		mat4.set_color(YELLOW)
		t4 = TextMobject("Thus the output", "vector","is")
		t4[1].set_color(YELLOW)


		t1.move_to(3*UP)
		t3.move_to(3*UP)
		mat.move_to(5*LEFT)
		t2.move_to(3*UP)
		mat2.move_to(3.5*LEFT)
		t4.move_to(3*UP)
		mat4.move_to(5*RIGHT)

		# self.add(grid)
		self.play(Write(t1))
		self.play(Transform(t1,mat))
		self.wait()
		self.play(Write(t2))
		self.play(Transform(t2,mat2))
		self.wait()
		self.play(Write(t3))
		self.play(Transform(t3,mat3))
		self.wait()
		self.play(Write(t4))
		self.play(Transform(t4,mat4))
		self.wait()


class Introduction_2(Scene):
	def construct(self):
		t1 = TextMobject("Now let's see how the","Transformation","looks visually")
		t1[1].set_color(YELLOW)
		self.play(Write(t1))
		self.wait()

class FinalTransformation(LinearTransformationScene):
    CONFIG = {
        "leave_ghost_vectors": True,
    }
    def construct(self):
        v = np.array([[1], [2]])
        matrix = [[-1, 1], [1, -1]]
        self.add_vector(v)
        self.apply_matrix(matrix)
        self.wait()