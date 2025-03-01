# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} color
# @return {Integer[][]}
def flood_fill(image, sr, sc, color)
    og_color = image[sr][sc]
    image[sr][sc] = color
    delta = [[0,1], [0, -1], [-1, 0], [1, 0]]
    delta.each do |x, y|
        nr, nc = sr + x, sc + y
        if nr >= 0 && nr < image.size && nc >= 0 && nc < image[0].size && image[nr][nc] == og_color && og_color != color
            image = flood_fill(image, nr, nc, color)
        end
    end
    image
end