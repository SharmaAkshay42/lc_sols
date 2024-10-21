class Solution:
	# m rows and n columns
	def uniquePaths(self, m: int, n: int) -> int:
		# Take an array of zeros below the last row
		prev_row = [0] * n

		# Start from the end 
		for r in range(m-1, -1, -1):
			curr_row = [0] * n 
			# There is only one path from the last column
			curr_row[-1] = 1
			for c in range(n - 2, -1, -1):
				# No. of paths at arr[r][c] = num_paths right + num_paths down
				curr_row[c] = curr_row[c+1] + prev_row[c]
			prev_row = curr_row

		# You build the table from end to start
		# Num of paths at [r][c] = num_paths to right + num_paths down
		return prev_row[0]