import sys
from PIL import Image, ImageDraw

def find_all_ovals(image):
    width, height = image.size
    visited = set()
    background_pixels = set()  # Pixels that can reach the edge
    fillable_regions = []

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and (x, y) not in visited

    def find_background_pixels():
        # Start from all edges and flood fill to find all transparent pixels
        # that have a path to the edge
        stack = []
        
        # Add all edge pixels that are transparent
        for x in range(width):
            if image.getpixel((x, 0))[3] == 0:
                stack.append((x, 0))
            if image.getpixel((x, height-1))[3] == 0:
                stack.append((x, height-1))
        
        for y in range(height):
            if image.getpixel((0, y))[3] == 0:
                stack.append((0, y))
            if image.getpixel((width-1, y))[3] == 0:
                stack.append((width-1, y))
        
        while stack:
            x, y = stack.pop()
            if (x, y) in background_pixels:
                continue
                
            background_pixels.add((x, y))
            
            # Check all adjacent pixels
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if image.getpixel((nx, ny))[3] == 0 and (nx, ny) not in background_pixels:
                        stack.append((nx, ny))

    def flood_fill_region(start_x, start_y):
        if not is_valid(start_x, start_y):
            return []
            
        region_pixels = []
        stack = [(start_x, start_y)]
        
        while stack:
            x, y = stack.pop()
            if not is_valid(x, y):
                continue
                
            current_pixel = image.getpixel((x, y))
            visited.add((x, y))
            
            if current_pixel[3] == 0 and (x, y) not in background_pixels:
                region_pixels.append((x, y))
            
            # Check all adjacent pixels
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    next_pixel = image.getpixel((nx, ny))
                    if next_pixel[3] == 0 or next_pixel[3] > 0:
                        stack.append((nx, ny))
        
        return region_pixels if region_pixels else []

    # First, find all transparent pixels that can reach the edge
    find_background_pixels()

    # Then find all regions, excluding background pixels
    for y in range(height):
        for x in range(width):
            if image.getpixel((x, y))[3] > 0 and (x, y) not in visited:
                region_pixels = flood_fill_region(x, y)
                if region_pixels:
                    fillable_regions.append(region_pixels)

    return fillable_regions

def flood_fill_oval_interior(image_path, output_path):
    # Open the image and keep it in RGBA mode
    image = Image.open(image_path).convert('RGBA')
    width, height = image.size
    
    # Create a new image with same size
    result = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    pixels = result.load()
    
    # Copy original image to result
    for y in range(height):
        for x in range(width):
            pixels[x, y] = image.getpixel((x, y))
    
    # Find all regions and fill them
    regions = find_all_ovals(image)
    
    for region in regions:
        # Fill all pixels in the region with white
        for x, y in region:
            pixels[x, y] = (255, 255, 255, 255)  # Make it white
    
    # Save the result
    result.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python flood_fill.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    flood_fill_oval_interior(input_image_path, output_image_path)