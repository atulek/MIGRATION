import numpy as np

class MIGRATION:
	def __init__(self):
		
		def migrate(self, pop, iter):
		for i in range(psize):
			if myrank == i:
				hedef = (myrank + 1) % psize
				MPI_Send(pop, nvar*MIG_RATE, MPI_DOUBLE, hedef, iter, MPI_COMM_WORLD)
			if myrank == (i + 1) % psize:
				kaynak = (myrank - 1) % pSize
				if kaynak<0:
					kaynak = kaynak + pSize
				MPI_Recv(&Man.gelen[0], nvar*MIG_RATE, MPI_DOUBLE, kaynak, iter, MPI_COMM_WORLD, &status)