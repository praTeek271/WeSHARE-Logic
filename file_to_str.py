import base64

def calculate_chunk_size(file_size, max_chunk_size):
    max_chunk_size = min(max_chunk_size, file_size)
    
    # Calculate the number of chunks needed to cover the file
    num_chunks = (file_size + max_chunk_size - 1) // max_chunk_size
    
    # Calculate adjusted chunk size for each file
    chunk_size = file_size // num_chunks
    return chunk_size

def file_to_chunks(file_path, max_chunk_size):
    # Read the file in binary format "rb"
    with open(file_path, 'rb') as file:
        binary_data = file.read()

    file_size = len(binary_data)
    print("file size\t",file_size)
    
    # use unique chunk size for each file , according to file size
    chunk_size = calculate_chunk_size(file_size, max_chunk_size)

    chunks = []
    for i in range(0, len(binary_data), chunk_size):
        chunk = binary_data[i:i + chunk_size]
        chunk_str = base64.b64encode(chunk).decode()
        chunks.append(chunk_str)
    packet_creator(chunks,file_path.split("/")[-1].split(".")[0])
    return len(chunk)

def chunks_to_file(lengt,name, output_file):
    y_data = b''
    for bfiles in range(2):
        binary_data = b''
        with(open(f"./output/{name}_{bfiles}.dat","rb")) as pkt_file:
            binary_data+=base64.encodebytes(pkt_file.read())
            chunk_data = base64.b64decode(binary_data)
            y_data+= chunk_data

             
    # convert the binary data back into file
    with open(output_file, 'wb') as file:
        file.write(binary_data)

def packet_creator(chunks,name):
    for id,data in enumerate(chunks):
        with(open(f"./output/{name}_{id}.dat",'w')) as file:
            string="{0}:{1}".format(id,str(data))
            file.write(string)
            file.close()
    print("created_packed........")
        
# Example usage:
file_path = './test_files/big-hero-6-2.png'
max_chunk_size = 2024  # Set the maximum desired chunk size (bytes)

# Break the file into chunks
chunks = file_to_chunks(file_path, max_chunk_size)
# print(chunks)
# print(len(chunks))

# Reassemble the chunks into a binary file
output_file = file_path.split("/")[-1]
chunks_to_file(2,file_path.split("/")[-1].split(".")[0],output_file)
