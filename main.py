from PIL import Image

# Open the GIF file
gif_path = 'pon.gif'
gif = Image.open(gif_path)

# Loop through each frame
frame_number = 0
while True:
    try:
        # Save or process the frame
        frame = gif.copy()  # Copy the frame to avoid overwriting
        frame.save(f'frames/frame_{frame_number}.png')  # Example: save each frame as a PNG file

        # Move to the next frame
        frame_number += 1
        gif.seek(frame_number)
    except EOFError:
        # When there are no more frames, an EOFError is raised
        break

print("All frames extracted.")
