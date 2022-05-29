import numpy as np

class MatrixHelper():

    def get_observed_object(width, height, device_matrix):
        '''
            This function returns the matrix that represents the 
            observed object in the entire observation matrix
        '''

        matrix = np.zeros((height,width),dtype=np.int8)

        # Intializes the matrix from the string
        for idx_row in range(height):     
            for idx_col in range(width):
                matrix[idx_row,idx_col] = device_matrix[idx_row*width+idx_col]

        # Remove all rows with only '0'
        m_nonzero_rows = matrix[[i for i, row in enumerate(matrix) if row.any()]]

        # Remove all columns with only '0'
        m_T = m_nonzero_rows.transpose()
        mT_nonzero_rows = m_T[[i for i, row in enumerate(m_T) if row.any()]]
        asteroid_matrix = mT_nonzero_rows.transpose()

        asteroid_height,asteroid_width = asteroid_matrix.shape

        # Flatten matrix to string
        asteroid_string = "".join([str(elem) for row in asteroid_matrix for elem in row])
        
        return {'height': asteroid_height, 'width': asteroid_width, 'string': asteroid_string}