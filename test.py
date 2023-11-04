# --------------------------------------------------------------------------------------------------

from SDP_offer_answer import SDPOfferAnswerGenerator, setup
import asyncio

async def main():
    sdp_gen = SDPOfferAnswerGenerator()
    
    # Create SDP offer
    await sdp_gen.create_offer()
    
    # Access SDP offer
    offer = sdp_gen.offer
    
    print("---------->offer -----==",offer)
    # Generate SDP answer (provide the offer as an argument)
    # answer = await sdp_gen.create_answer(offer).answer
    # print(answer)
if __name__ == '__main__':
    a=setup()
    import asyncio
    asyncio.run(main())

# import base64

# def calculate_chunk_size(file_size, max_chunk_size):
#     # Set a maximum chunk size to ensure it's not too large
#     max_chunk_size = min(max_chunk_size, file_size)
    
#     # Calculate the number of chunks needed to cover the file
#     num_chunks = (file_size + max_chunk_size - 1) // max_chunk_size
    
#     # Calculate the adjusted chunk size
#     chunk_size = file_size // num_chunks
#     return chunk_size

# def file_to_chunks(file_path, max_chunk_size):
#     # Read the binary content of the file
#     with open(file_path, 'rb') as file:
#         binary_data = file.read()

#     file_size = len(binary_data)
    
#     # Calculate the adjusted chunk size based on file size
#     chunk_size = calculate_chunk_size(file_size, max_chunk_size)

#     chunks = []
#     for i in range(0, len(binary_data), chunk_size):
#         chunk = binary_data[i:i + chunk_size]
#         # Convert each chunk into a base64-encoded string
#         chunk_str = base64.b64encode(chunk).decode()
#         chunks.append(chunk_str)

#     return chunks

# def chunks_to_file(chunks, output_file):
#     binary_data = b''
#     for chunk_str in chunks:
#         # Convert the base64-encoded string back to binary
#         chunk = base64.b64decode(chunk_str)
#         binary_data += chunk

#     # Save the binary data as a file
#     with open(output_file, 'wb') as file:
#         file.write(binary_data)

# # Example usage:
# file_path = './test_files/big-hero-6-2.png'
# max_chunk_size = 1024  # Set the maximum desired chunk size (bytes)

# # Break the file into chunks
# chunks = file_to_chunks(file_path, max_chunk_size)

# # Transfer the chunks over the network (simulated here)

# # Reassemble the chunks into a binary file
# output_file = 'reconstructed.png'
# chunks_to_file(chunks, output_file)
# print("done")
