import numpy as np
import logging

class RasPiUtilities:

    def array_to_file(a1, new_file_name):

        '''Takes a numpy array (1-D or 2-D) or Python list (1-D or 2-D) of bytes (numpy.dtype="S1"),
        and writes its data to a file.

         Arguments:
             a1 :               a 1-D or 2-D Python list, or Numpy array/matrix
             new_file_name :    name of new text file to be created.'''

        # --------------------------------------------------------------------------------------------------------------
        # (1)
        # Initialization and configuration of logging.
        # Block Inputs : None

        logging.basicConfig(filename="array_to_file.log", format='%(asctime)s : %(message)s', level=logging.DEBUG)
        logging.info("Using function 'array_to_file'.")

        # Block Outputs : None
        # (1)
        # --------------------------------------------------------------------------------------------------------------
        # (2)
        # Try to open a new file for writing to, with the given name.
        # Block Inputs : (new_file_name)

        try:
            fout = open(new_file_name, "w")
        except Exception as err1:
            logging.debug("Error opening file for writing:")
            logging.debug(err1)

        # Block Outputs : (fout)
        # (2)
        # --------------------------------------------------------------------------------------------------------------
        # (3)
        # If file opened successfully for writing, code for reading the input array passed into 'a1'
        # Block Inputs: (a1,fout)

        else:
            try:
                for val in a1:

                    # --------------------------------------------------------------------------------------------------
                    # (3.1)
                    # If array passed in is a 2-Dimensional Numpy Array, or a 2-Dimensional/Nested List,
                    # the element of the outer array/list will also itself be an array/list:
                    # Block Inputs: (val, fout)

                    if isinstance(val, np.ndarray) or isinstance(val, list):
                        for element in val:
                            print(type(element))
                            print(element)
                            fout.write(str(element))
                            fout.write(",")
                            # logging.info("Writing to file:")
                            # logging.info(element)
                        fout.write("\n")

                    # Block Outputs: (val,fout)
                    # (3.1)
                    # --------------------------------------------------------------------------------------------------
                    # (3.2)
                    # If array passed in is a One-dimensional Numpy Array or List:
                    # Block Inputs: (val, fout)

                    else:
                        print(val)
                        fout.write(str(val))
                        logging.info(val)
                        fout.write(",")

                    # Block Outputs: (fout)
                    # (3.2)
                    # --------------------------------------------------------------------------------------------------

                # After done writing, close file.
                fout.close()
                # --
            # ----------------------------------------------------------------------------------------------------------
            # (3.3)
            # In case of any error in writing the array contents to file, log the error, else, log a success message.
            # Block Inputs: None

            except Exception as err2:
                logging.debug("Error in writing to file:")
                logging.debug(err2)
            else:
                logging.info("Array-to-file operation successful!")

            # Block Outputs: None
            # (3.3)
            # ----------------------------------------------------------------------------------------------------------
        # Block Outputs: None
        # (3)-----
        # --------------------------------------------------------------------------------------------------------------
    # End of function 'array_to_file'


    def file_to_array(file_name):

        ''' Takes a text file (csv) with byte values, extracts the file's data and puts it into a Numpy array/matrix,
        and returns the array/matrix.
        Arguments:
            file_name: name of file which is to be read.
        '''

        # --------------------------------------------------------------------------------------------------------------
        # (1)
        # Open a new file for writing.
        # Initialize an array for storing final result to return
        # Block Inputs: (file_name)

        fin = open(file_name, "r")
        final_arr = []

        # Block Outputs: (fin, final_arr)
        # (1)
        # --------------------------------------------------------------------------------------------------------------
        # (2)
        # Extract each value from the (csv) text file, convert it to a bytes object, and
        # store it in a list.
        # Block Inputs: (fin, final_arr)

        for line in fin:

            elements = line.split(",")[:-1]
            intermediate_arr = []

            for val in elements:
                b1 = bytes.fromhex(val[4:-1])
                intermediate_arr.append(b1)

            final_arr.append(intermediate_arr)

        fin.close()

        # Block Outputs: (final_arr)
        # (2)
        # --------------------------------------------------------------------------------------------------------------
        # (3)
        # Convert the 'final_arr' list to a Numpy object with dtype='S1' (to match the input to the 'RasPiUtilities.array_to_file' function.
        # and return the Numpy array/matrix object.
        # Block Inputs: (final_arr)

        final_arr = np.array(final_arr, dtype="S1")
        return final_arr

        # Block Outputs: None
        # (3)
        # --------------------------------------------------------------------------------------------------------------
    # End of function 'file_to_array'